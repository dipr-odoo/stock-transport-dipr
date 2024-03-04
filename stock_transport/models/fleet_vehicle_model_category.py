from odoo import fields, models


class FleetVehicleModelCategory(models.Model):
    _inherit='fleet.vehicle.model.category'

    max_weight=fields.Float(string = "Max Weight (Kg)")
    max_volume=fields.Float(string = "Max Volume (m^3)")
    # max_weight=fields.Integer()
    # max_volume=fields.Integer()

    def _compute_display_name(self):
        for category in self:
            display_name = category.name
            if category.max_weight or category.max_volume:
                display_name += f" ({category.max_weight} kg, {category.max_volume} m^3)"
            category.display_name = display_name

