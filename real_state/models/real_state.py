from odoo import models, fields


class RealState(models.Model):
    _name = "real.state"
    _description = "real state"

    name = fields.Char()
    description = fields.Text()
    postcode = fields.Char()
    date_availability = fields.Date()
    expected_price = fields.Float()
    bedrooms = fields.Integer()
    garage = fields.Boolean()
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')])