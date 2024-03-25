# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Guru(models.Model):
    _name = 'guru'
    _description = 'Model guru'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nama guru', required=True)
    mapel = fields.Many2one('mata.pelajaran', 'Mata pelajaran', required=True)



