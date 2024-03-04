from odoo import fields, models

class StockDock(models.Model):
    _name='stock.dock'
    _description= 'Custom docks'

    name=fields.Char(required = True, string ="Dock")
    
