# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Stock(models.Model):
    _name = "stock"
    _description = "库存"
    _order = "create_date, id desc"

    move_ids = fields.One2many(string="库存出入记录", comodel_name="stock.move", inverse_name="stock_id")

    # def action_sum(self):
    #     for record in self:
    #         for move in record.move_ids:
    #

