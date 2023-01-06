from werkzeug.exceptions import BadRequest

from odoo.http import request
from odoo import models


class Http(models.AbstractModel):
    _inherit = 'ir.http'

    @classmethod
    def _auth_method_token(cls):
        api_key = request.httprequest.headers.get("Authorization")

        if not api_key:
            raise BadRequest("Authorization header with API key missing")

        token = request.env['auth_token.token'].sudo().search([('active', '=', True), ('token', '=', api_key)])

        if not token:
            raise BadRequest("API key invalid")

        request.update_env(user=token.user_id.id)
