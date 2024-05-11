from odoo import models, fields


class SaleOrder(models.Model):
    _inherits = 'sale.order'

    total_amount = fields.Integer()
