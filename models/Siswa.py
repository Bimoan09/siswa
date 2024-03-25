# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Siswa(models.Model):
    _name = 'siswa'
    _description = 'Model siswa'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Nama siswa', required=True)
    date_of_birth = fields.Date(string='Tanggal lahir',required=True)
    kelas = fields.Many2one('kelas', string='Kelas', required=True)
    guru = fields.Many2one('guru', string='Guru', required=True)
    mata_pelajaran = fields.Many2one('mata.pelajaran', related="guru.mapel", string='Mata pelajaran')


