# -*- coding: utf-8 -*-
{
    'name': "Frontend Paper",

    'author': "Nileshkumar Vaghela",
    'website': "http://www.aktivsoftware.com",

    'category': 'Website',
    'version': '15.0.1.0.0.',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'sale'],


    # always loaded
    'data': [
        'security/shop_message_security.xml',
        'views/res_config_setting.xml',
        'views/website_template.xml',
    ],

    'license': 'LGPL-3',
}
