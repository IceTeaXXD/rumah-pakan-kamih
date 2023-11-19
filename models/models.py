from odoo import models, fields, api

class Stock(models.Model):
    _name = 'rpk.stock'

    name = fields.Char(string='Name')
    quantity = fields.Integer(string='Quantity', compute='_compute_quantity')

    log_ids = fields.One2many('rpk.log', 'stock_id', string='Logs')

    @api.depends('log_ids', 'log_ids.change')
    def _compute_quantity(self):
        for record in self:
            record.quantity = sum(log.change for log in record.log_ids)

class Log(models.Model):
    _name = 'rpk.log'

    date = fields.Date(string='Date')
    description = fields.Text(string='Description')
    change = fields.Integer(string='Change')
    stock_id = fields.Many2one('rpk.stock', string='Stock')

class Catalog(models.Model):
    _name = 'rpk.catalog'

    name = fields.Char(string='Room Name')
    price = fields.Float(string='Price')
    description = fields.Text(string='Description')
    image = fields.Binary(string='Image')
    reservation_ids = fields.One2many('rpk.reservation', 'catalog_id', string='Bookings')


class Reservation(models.Model):
    _name = 'rpk.reservation'

    date_start = fields.Date(string='Date Start')
    date_end = fields.Date(string='Date End')
    catalog_id = fields.Many2one('rpk.catalog', string='Room')

