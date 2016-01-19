from tornado import options, httpserver
from tornado.escape import json_decode, json_encode
import tornado.gen
import tornado.web
import tornado
from cn.decorators import authentication
from cn.mixins import AsyncClientMixin
from proxy import MyConnectorProxy
from settings import *

ioloop = tornado.ioloop.IOLoop.instance()


class BaseHandler(AsyncClientMixin, tornado.web.RequestHandler):
    """
    Base class for handler response
    """

    def response_handler(self, data):
        self.write(json_encode(data))

class MyConnectorActionsHandler(BaseHandler):
    """
    Handler for 'actions' requests
    """

    @authentication(AUTH_CHECK_TOKEN_URL)
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # Get request params
        kwargs = json_decode(self.request.body)
        # Create proxy object instance
        my_conn = MyConnectorProxy()
        # Check if 'action' from params exists in proxy instance
        action = getattr(my_conn, 'action_%s' % kwargs['action'], None)
        if action:
            # Run action
            response = yield action(**kwargs)
            self.response_handler(response)


class MyConnectorMethodsHandler(BaseHandler):
    """
    Handler for 'methods' requests
    """
    @authentication(AUTH_CHECK_TOKEN_URL)
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def get(self):
        # Get method name
        method_name = self.get_argument('method')
        # Get user_id parameter
        user_id = self.get_argument('user_id')
        # Create instance of connector object
        my_conn = MyConnectorProxy()
        # Search method callback in connector object
        method = getattr(my_conn, 'method_%s' % method_name, None)
        kwargs = {
            'user_id': user_id
        }
        # Run method
        if method:
            response = yield method(**kwargs)
            self.response_handler(response)


class MyConnectorTriggersHandler(BaseHandler):
    """
    Handler for 'trigger' requests
    """
    @authentication(AUTH_CHECK_TOKEN_URL)
    @tornado.web.asynchronous
    @tornado.gen.coroutine
    def post(self):
        # Get request params
        kwargs = json_decode(self.request.body)
        # Create proxy object instance
        my_conn = MyConnectorProxy()
        # Check if 'trigger' from params exists in proxy instance
        trigger = getattr(my_conn, 'trigger_%s' % kwargs['trigger'], None)
        if trigger:
            # Run trigger
            response = yield trigger(**kwargs)
            self.response_handler(response)


app_settings = {}

# Generate tornado webserver application
def get_application(app_settings):
    return tornado.web.Application([
        (r"/actions", MyConnectorActionsHandler),
        (r"/methods", MyConnectorMethodsHandler),
        (r"/triggers", MyConnectorTriggersHandler),
    ], **app_settings)

application = get_application(app_settings)


def main():
    """
    Main function of worker file
    """
    
    print("My Connector")
    print(PORT)
    # Create instance of proxy
    proxy = MyConnectorProxy()

    # Registrate connector in Apination system
    ioloop.call_later(PROXIES_REGISTER_AFTER_SECONDS, proxy.register_self)

    # Start http server
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(PORT)

    ioloop.start()

# Run main() on script start
if __name__ == "__main__":
    main()
