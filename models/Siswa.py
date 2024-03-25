# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Siswa(models.Model):
    _name = 'siswa'
    _description = 'Model siswa'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nama siswa')
    date_of_birth = fields.Date(string='Tanggal lahir')
    kelas = fields.Many2one('kelas', string='Kelas')
    guru = fields.Many2one('guru', string='Guru')
    mata_pelajaran = fields.Many2one('mata.pelajaran', related="guru.mapel", string='Mata pelajaran')


