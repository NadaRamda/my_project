# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from odoo.exceptions import ValidationError
from datetime import date
from dateutil.relativedelta import relativedelta



class ResPartner(models.Model):
    _inherit = "res.partner"


    is_student = fields.Boolean(required=True)
    birth_date = fields.Date()
    age = fields.Integer(compute='_compute_age', store=True)

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                print(rec.birth_date)
                rec.age = relativedelta(date.today(),rec.birth_date).years
                # rec.age = date.today().year - rec.birth_date.year
                print(rec.age)
                if not rec.age in range (4 ,5):
                    raise ValidationError(_(
                        "Age must be in range 4-5 years."
                    ))
            else:
                rec.age = 0






