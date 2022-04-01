# -*- coding: utf-8 -*-
{
    'name': "Student",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale', 'contacts'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/sale.xml',
        'views/depends_contacts.xml',
        'views/con_setting.xml',
        'views/views.xml',

    ],
    # only loaded in demonstration mode
    'license': 'LGPL-3',
    
}
