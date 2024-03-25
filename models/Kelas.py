# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Kelas(models.Model):
    _name = 'kelas'
    _description = 'Model kelas'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char('Nama kelas')




