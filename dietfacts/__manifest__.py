 #-*- coding: utf-8 -*-
{
    'name': "Mx_Dietfacts",

    'summary': """
        learning
    """,

    'description': """
        description
    """,

    'author': "Maxware",
    'website': "http://www.maxware.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctl
    'depends': ["base"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'instalable':True,
    'application':True,
    'auto_install':False,
}