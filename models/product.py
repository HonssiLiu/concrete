# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Product(models.Model):
    _name = "product"
    _description = "产品"
    _order = "sequence, name asc"
    _sql_constraints = [
        ('product_account_id', 'unique (account_id)', "会计科目编号必须唯一！"),
    ]

    sequence = fields.Integer(string='序号', default=1)
    account_id = fields.Char(string="会计科目编号", required=True)
    name = fields.Char(string="名称", required=True)
    unit = fields.Char(string="单位")
    is_buy = fields.Boolean(string="可采购", default=0)
    is_sell = fields.Boolean(string="可销售", default=0)
    is_product = fields.Boolean(string="可生产", default=0)

    quantity = fields.Float(string="总数量", default=0)
    amount = fields.Float(string="总金额", compute="_compute_amount", store=True, default=0)
    price = fields.Float(string="总单价", compute="_compute_price", store=True, default=0)

    @api.depends("amount", "quantity")
    def _compute_price(self):
        for record in self:
            if record.quantity != 0:
                record.price = record.amount / record.quantity

    @api.depends("price", "quantity")
    def _compute_amount(self):
        for record in self:
            record.amount = record.price * record.quantity


