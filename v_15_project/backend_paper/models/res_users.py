from odoo import api, models, modules


class Users(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        result = []

        for user_rec in self:
            if user_rec.name:
                result.append((user_rec.id, '%s , %s' % (user_rec.name, user_rec.city)))
            else:
                result.append((user_rec.id, '{}'.format(user_rec.name)))

        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=50, name_get_uid=None):
        args = args or []
        domain = []

        if name:
            domain = ['|', ('city', operator, name), ('name', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)
