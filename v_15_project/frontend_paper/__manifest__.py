# -*- coding: utf-8 -*-
{
    'name': "frontend_paper",

    'author': "Nileshkumar Vaghela",
    'website': "http://www.aktivsoftware.com",

    'category': 'Website',
    'version': '15.0.1.0.0.',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website'],


    # always loaded
    'data': [
        'views/create_contact_form_template.xml',
        'views/account_existing_record.xml',
    ],

    'assets': {
        'web.assets_frontend': [
            'frontend_paper/static/src/css/frontend.css',
        ]
    },
    'license': 'LGPL-3',
}
