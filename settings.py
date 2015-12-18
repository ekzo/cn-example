import os

PORT = os.environ.get('PORT', 8080)
PROXIES_REGISTER_AFTER_SECONDS = int(os.environ.get('PROXIES_REGISTER_AFTER_SECONDS', 30))

HUB_URL = os.environ.get('HUB_URL', 'http://hub-stg.apination.com/')
HUB_ONTRIGGER_URL = HUB_URL + os.environ.get('HUB_ONTRIGGER_URL', 'ontrigger')
HUB_REGISTER_PROXY_URL = HUB_URL + os.environ.get('HUB_REGISTER_PROXY_URL', 'register/proxy')
HUB_GET_TRIGGER_LIST_URL = HUB_URL + os.environ.get('HUB_GET_TRIGGER_LIST_URL', 'triggers')

AUTH_PUBLIC = os.environ.get('AUTH_PUBLIC', '<get from Apination administrator>')
AUTH_SECRET = os.environ.get('AUTH_SECRET', '<get from Apination administrator>')
