from odoo import api, fields, models

class FleetVehicleModel(models.Model):
    _inherit = 'fleet.vehicle.model'
    

    def _compute_display_name(self):
        for model in self:
           if model.category_id:
            model.display_name = f'{model.brand_id.name}/{model.name} ({model.category_id.name})'

    

