import random
import string

from odoo import api, models, fields


class Token(models.Model):
    _name = "auth_token.token"

    @staticmethod
    def _get_random_string(l=7):
        return ''.join(random.choices(string.ascii_lowercase + string.digits, k=l))

    @staticmethod
    def _generate_token():
        return '-'.join([Token._get_random_string() for x in range(4)])

    @api.model
    def default_get(self, fields):
        res = super().default_get(fields)
        res.update({'token': Token._generate_token()})

        return res

    token = fields.Char('Token')
    active = fields.Boolean('Active')
    user_id = fields.Many2one('res.users', string='User')


class User(models.Model):
    _inherit = 'res.users'

    token_ids = fields.One2many('auth_token.token', 'user_id')