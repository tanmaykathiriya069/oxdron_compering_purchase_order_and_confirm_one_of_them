# -*- coding: utf-8 -*-

from odoo import models, _

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    _description = 'Purchase Order Line'

    def action_choose(self):
        order_lines_id = (self.order_id | self.order_id.alternative_po_ids).mapped('order_line')
        order_lines = order_lines_id.filtered(lambda l: l.product_qty and l.product_id.id in self.product_id.ids and l.id not in self.ids)
        if order_lines:
            order_lines.action_clear_quantities()
            if order_lines.order_id:
                purchase_order_cancelled = ", ".join(order_lines.mapped('order_id.name'))
                final_order = ", ".join(set(order_lines_id.mapped('order_id.name')) - set(order_lines.mapped('order_id.name')))
                fail_reason = f"This all purchase orders ({purchase_order_cancelled}) canceled because of I have ({final_order}) favorable purchase order."
                for purchase in order_lines.order_id:
                    purchase.message_post(body=fail_reason)
                    purchase.button_cancel()
            return True
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': _("Nothing to clear"),
                'message': _("There are no quantities to clear."),
                'sticky': False,
            }
        }
