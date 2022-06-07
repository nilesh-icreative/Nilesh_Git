# -*- coding: utf-8 -*-
{
    'name': "backed_paper",

    'author': "Nileshkumar Vaghela",
    'website': "http://www.aktivsoftware.com",

    'category': 'sale.order',
    'version': '15.0.1.0.0.',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
    ],
    'license': 'LGPL-3',
}
