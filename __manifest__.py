# -*- coding: utf-8 -*-

{
    'name': "Purchase Order Line Customization",
    'summary': "Customizes the behavior of purchase order lines.",
    'description': """
        This module customizes the behavior of purchase order lines in Odoo. 
        It enhances the functionality of the action_choose method to cancel pending purchase orders and display notifications to users.
    """,
    'author': " Mr. Tanmay Kathiriya - Odoo Developer",
    'website': "",
    'category': 'Purchases',
    'version': '17.0.0.1',
    'depends': ['base', 'purchase_requisition'],
    'data': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
