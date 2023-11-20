# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class Cat(models.Model):
#     _name = 'cats.cat'
#     _description = 'Deskripsi Kucing'


#     name = fields.Char(string="Nama", required=True)
#     color = fields.Selection(selection=[
#         ('0', 'Merah'), ('1', 'Kuning'), ('2', 'Hijau'), ('3', 'Biru'), ('4', 'Ungu'), 
#     ], string="Warna", required=True)
#     type = fields.Many2one('cats.cat.type', string="Jenis")


# class CatType(models.Model):
#     _name = 'cats.cat.type'
#     _description = 'Jenis Kucing'


#     name = fields.Char(string="Nama")

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
