# -*- coding: utf-8 -*-

from odoo import models, fields, api


class MataPelajaran(models.Model):
    _name = 'mata.pelajaran'
    _description = 'Model Mata Pelajaran'
    _inherit = ['mail.thread', 'mail.activity.mixin']



    name = fields.Char('Mata pelajaran')




