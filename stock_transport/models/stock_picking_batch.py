from odoo import api,fields, models


class StockPickingBatch(models.Model):
    _inherit = 'stock.picking.batch'

    dock_id = fields.Many2one('stock.dock', string = "Dock")
    vehicle_id = fields.Many2one('fleet.vehicle.model', string = "Vehicle")
    # category_id = fields.Many2one('fleet.vehicle.model.category', string = 'Vehicle Category')
    category_id = fields.Many2one('fleet.vehicle.model.category', string = 'Vehicle Category', compute="_compute_cat")
    weight_bar = fields.Float(compute="_compute_wb", store = True)
    total_weight= fields.Float(compute="_compute_weight", store = True)
    volume_bar = fields.Float(compute="_compute_vb", store=True)
    total_volume = fields.Float(compute="_compute_volume", store=True)
    no_of_transfers = fields.Integer(compute="_compute_no_of_transfers", store=True)
    no_of_lines = fields.Integer(compute="_compute_no_of_lines", store=True)
    
    @api.depends('picking_ids')
    def _compute_no_of_transfers(self):
        for record in self:
            record.no_of_transfers = len(record.picking_ids)

    @api.depends('move_line_ids')
    def _compute_no_of_lines(self):
        for record in self:
            record.no_of_lines = len(record.move_line_ids)
    

    @api.depends("vehicle_id")
    def _compute_cat(self):
        for record in self:
            record.category_id= record.vehicle_id.category_id

    @api.depends("picking_ids")
    def _compute_weight(self):
        for record in self:
            total_weight = 0.0
            for picking in record.picking_ids:
                total_weight += picking.weight
            record.total_weight = total_weight
    
    @api.depends('total_weight', 'category_id')
    def _compute_wb(self):
        for record in self:
            if record.total_weight and record.category_id.max_weight:
                record.weight_bar = (record.total_weight / record.category_id.max_weight) * 100
            else:
                record.weight_bar = 0.0
    
    @api.depends("picking_ids")
    def _compute_volume(self):
        for record in self:
            total_volume = 0.0
            for picking in record.picking_ids:
                total_volume += picking.volume
            record.total_volume = total_volume
    
    @api.depends('total_volume', 'category_id')
    def _compute_vb(self):
        for record in self:
            if record.total_volume and record.category_id.max_volume:
                record.volume_bar = (record.total_volume / record.category_id.max_volume) * 100
            else:
                record.volume_bar = 0.0
    
    def _compute_display_name(self):
        for record in self:
            record.display_name = record.name
            if record.total_weight:
                record.display_name += f' ({record.total_weight} kg)'
            if record.total_volume:
                record.display_name += f' ({record.total_volume} m^3)'








