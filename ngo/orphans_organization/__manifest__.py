# -*- coding: utf-8 -*-
{
    'name': "orphans_organization",

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
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/ngo_bool.xml',
        'views/views.xml',
        'views/wizards.xml',
        'views/o_donation.xml',
        'views/org_sub_action.xml',
        'views/orphans_orga.xml',

        'views/expense_type.xml',
        'views/orphans_expense.xml',
        'views/orphans_advertise.xml',
        'views/member_sub_action.xml',
        'views/o_member.xml',

        'reports/donations_report_template.xml',
        'reports/donation_report_format.xml',
        'reports/donation_report_actions.xml',

        'views/action.xml',
        'views/menu_item.xml',
    ],
    # only loaded in demonstration mode

    'license':'LGPL-3',

}
