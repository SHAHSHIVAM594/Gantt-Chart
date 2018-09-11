# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import _, api, exceptions, fields, models


class JsonParse(models.Model):
    _name = "json.model"

    name = fields.Char("Name")
    author = fields.Char("Author")
    types = fields.Char("Type")
    startdate = fields.Datetime("Start Date")
    enddate = fields.Datetime(string="End Date")
    status = fields.Char("Status")

    @api.constrains('startdate', 'enddate')
    def _compute_name(self):
        if self.enddate < self.startdate:
            raise exceptions.ValidationError(_("Enddate is always after startdate"))
