"""
Connector registration data
"""

CONNECTOR_REGISTER_DATA = {
    'full_name': 'My Connector',
    'company_name': 'My Company',
    'description': 'Description of my connector',
    'name': 'my_connector',
    'proxy_url': 'http://my_connector.example.com',
    'app_page_info': {
        'actions': [
            {
                'title': 'My action',
                'description': 'Description of my action'
            }
        ],
        'triggers': [
            {
                'title': 'My trigger',
                'description': 'Description of my trigger'
            },
        ]
    },
    'actions': [
        {
            'name': 'my_action',
            'params': [
                {
                    'name': 'user_id',
                    'required': True
                },
                {
                    'name': 'post_args',
                    'description': 'Post arguments in request',
                    'required': True
                }
            ]
        }
    ],
    'methods': [
        {
            'name': 'my_method',
            'params': [
                {
                    'name': 'user_id',
                    'required': True
                }
            ]
        }
    ],
    'triggers': [
        {
            'name': 'my_trigger',
            'params_for_reg': [
                {
                    'name': 'user_id',
                    'required': True
                },
                {
                    'name': 'conditions',
                    'required': False
                }
            ]
        },
    ]
}
