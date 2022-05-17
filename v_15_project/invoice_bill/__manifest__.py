# -*- coding: utf-8 -*-
{
    'name': "invoice_bill",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nilesh Vaghela",
    'website': "http://www.aktivsoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/
    # addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'invoice',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/account_move_line.xml',
        'views/account_move.xml',

    ],
    'license': 'LGPL-3',
    # only loaded in demonstration mode

}
