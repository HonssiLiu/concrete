# -*- coding: utf-8 -*-

from datetime import timedelta
from odoo import api, fields, models
from odoo.exceptions import UserError, ValidationError


class Purchase(models.Model):
    _name = "concrete.purchase"
    _order = "id desc"
