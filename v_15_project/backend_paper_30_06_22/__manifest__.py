# -*- coding: utf-8 -*-
{
    'name': "Backend Practical",

    'author': "Nileshkumar Vaghela",
    'website': "http://www.aktivsoftware.com",

    'category': 'Sales',
    'version': '15.0.1.0.0',


    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_views.xml',
        'views/product_views.xml',
        'views/sale_order_line_view.xml',
        'views/sale_quotation_report.xml',
        'views/account_move_line.xml',
    ],
    'application': True,
    'license': 'LGPL-3',
}
