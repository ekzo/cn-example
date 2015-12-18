import tornado
from tornado.escape import json_encode
import tornado.ioloop
import tornado.web
from cn.proxy import BaseProxy
from register import CONNECTOR_REGISTER_DATA
from settings import AUTH_PUBLIC, AUTH_SECRET, HUB_REGISTER_PROXY_URL
from cn.mixins import AsyncClientMixin
from constants import HTTP_METHOD_POST
from cn.utils import auth_headers_request
from tornado.httpclient import HTTPRequest, HTTPResponse
from io import BytesIO


class MyConnectorProxy(AsyncClientMixin, BaseProxy):
    """
    Skeleton of Connector Proxy class
    """
    @tornado.gen.coroutine
    def register_self(self):
        """
        Register connector in Apination system
        """
        super().register_self()
        client = self.get_async_http_client()
        response = yield client.fetch(
                HUB_REGISTER_PROXY_URL,
                method=HTTP_METHOD_POST,
                body=tornado.escape.json_encode(CONNECTOR_REGISTER_DATA),
                headers=auth_headers_request(AUTH_PUBLIC, AUTH_SECRET))
        return response

    @tornado.gen.coroutine
    def action_my_action(self, *args, **kwargs):
        """
        Skeleton of connector action
        """
        user_id = kwargs.get('user_id')
        return {"status": "success", "data": {"action": "my action", "user_id": user_id}}

    @tornado.gen.coroutine
    def trigger_my_trigger(self, *args, **kwargs):
        """
        Skeleton of connector trigger
        """
        return {"status": "success", "data": {"trigger": "my trigger"}}

    @tornado.gen.coroutine
    def method_my_method(self, *args, **kwargs):
        """
        Skeleton of connector method
        """
        return {"status": "success", "data": {"hello": "world", "method": "my method"}}
