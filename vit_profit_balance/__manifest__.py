# -*- coding: utf-8 -*-
{
    'name': "vit_profit_balance",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "yusup",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','mis_builder','vit_mis_kisel'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'data_profit/mis.report.csv',
        'data_profit/mis.report.kpi.csv',
        'data_profit/mis.report.instance.csv',
        'data_balance/mis.report.csv',
        'data_balance/mis.report.kpi.csv',
        'data_balance/mis.report.instance.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}