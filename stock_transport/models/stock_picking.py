from odoo import api, fields, models

class StockPicking(models.Model):
    _inherit= "stock.picking"

    weight= fields.Float(compute= "_compute_weight_vol", default =0, store= True)
    volume = fields.Float(compute = "_compute_weight_vol", default =0, store= True)
    # weight= fields.Integer(default = 0)
    # volume = fields.Integer(default =0)

    @api.depends("move_ids")
    def _compute_weight_vol(self):
        # print("=======================",self)
        for record in self:
            # print("=======================",record)
            total_weight = 0
            total_volume = 0
            for move in record.move_ids:
                # print("=======================",move.product_id.weight,"============",move.product_id.volume)

                total_weight += move.product_id.weight * move.quantity
                total_volume += move.product_id.volume * move.quantity
            # print("******",total_volume,"***",total_weight)
            record.weight = total_weight
            record.volume = total_volume
