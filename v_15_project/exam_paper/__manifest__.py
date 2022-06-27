# -*- coding: utf-8 -*-
{
    'name': "Exam Paper",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'author': "Nileshkumar Vaghela",
    'website': "http://www.aktivsoftware.com",

    'category': 'Sale',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/contact_views.xml',
        'views/res_config_setting_view.xml',
        'views/mail_template_limit_customer.xml',
    ],

    'license': 'LGPL-3',

}
