# -*- coding: utf-8 -*-
{
    'name': "backed_paper",

    'author': "Nileshkumar Vaghela",
    'website': "http://www.aktivsoftware.com",

    'category': 'sale.order',
    'version': '15.0.1.0.0.',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'wizards/product_view.xml',
        'views/views.xml',
        'views/product_view.xml',
        'views/sale_order_view.xml',
        'views/sale_order_line_view.xml',
        
    ],
    'application': True,
    'license': 'LGPL-3',
}
