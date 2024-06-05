# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class StockMove(models.Model):
    _name = "stock.move"
    _description = "库存出入记录"
    _order = "create_date, id desc"

    create_date = fields.Date(string="日期", default=fields.Date.today())
    product_id = fields.Many2one(string="产品", comodel_name="product")
    quantity = fields.Float(string="数量", default=0)
    amount = fields.Float(string="金额", compute="_compute_amount", store=True, default=0)
    price = fields.Float(string="单价", compute="_compute_price", store=True, default=0)

    stock_id = fields.Many2one(string="库存", comodel_name="stock")

    @api.depends("amount", "quantity")
    def _compute_price(self):
        for record in self:
            if record.quantity != 0:
                record.price = record.amount / record.quantity

    @api.depends("price", "quantity")
    def _compute_amount(self):
        for record in self:
            record.amount = record.price * record.quantity
