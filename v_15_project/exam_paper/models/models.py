# -*- coding: utf-8 -*-

from odoo import models, fields, api


class exam_paper(models.Model):
    _name = 'exam_paper'
    _description = 'exam_paper'

    name = fields.Char()
