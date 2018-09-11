# -*- coding: utf-8 -*-
{
    'name': "Odoo deliverable task",

    'summary': "Odoo Project",

    'description': """
                Demo Project
    """,

    'version': '1.0',

    'depends': [
      'base',
      'website',
    ],

    'data': [
       'views/json_model_views.xml',
    ],

    'qweb': [
        "static/src/xml/dialog.xml",
    ],

    'application': True,
    'installable': True
}
