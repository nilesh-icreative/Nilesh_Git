# -*- coding: utf-8 -*-
{
    'name': "orphans_organization",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Nilesh Vaghela",
    'website': "http://www.aktivsoftware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo
    # /addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Ngo',
    'version': '15.0.1.0.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/expense_type.xml',
        'views/ngo_bool.xml',
        'views/views.xml',
        'views/wizards.xml',
        'views/sent_mail_request_user.xml',
        'views/o_donation.xml',
        'views/org_sub_action.xml',
        'views/orphans_orga.xml',

        'views/expense_type.xml',
        'views/orphans_expense.xml',
        'views/orphans_advertise.xml',
        'views/member_sub_action.xml',
        'views/o_member.xml',

        'views/reports.xml',

        'reports/donations_report_template.xml',
        'reports/donation_report_format.xml',
        'reports/donation_report_actions.xml',

        'views/action.xml',
        'views/menu_item.xml',
    ],
    # only loaded in demonstration mode

    'license': 'LGPL-3',

}
