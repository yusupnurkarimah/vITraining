# -*- coding: utf-8 -*-
{
    'name': "vit_stages_invoice",

    'summary': """
        - Menambahkan field stage di account.invoice
        - Manambahkan group by stages
        """,

    'description': """
        Long description of module's purpose
    """,

    'author': "yusup[vitraining.com]",
    'website': "http://www.vitraining.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/vit_stages_invoice.stage.csv',
        'views/views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}