# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import http
from odoo.http import request

class WebsiteDepartment(http.Controller):
    @http.route("/authors/search", type="json", auth="public")
    def all_authors(self, author):
        Authors = request.env['json.model'].search([('author', '=', author)])
        mylist = []
        for rec in Authors:
            mylist.append
            ({
                'author': rec.author,
                'taskName': rec.name,
                'types': rec.types,
                'startdate': rec.startdate,
                'enddate': rec.enddate,
                'status': rec.status
            })
        return mylist
