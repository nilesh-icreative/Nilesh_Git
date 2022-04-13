
from odoo import models , api , fields


class saleview(models.Model):

    _inherit = 'res.partner'

    def name_get(self):
        result = []

        for rec in self:
            if rec.customer_r:
                result.append((rec.id, '%s , %s' % (rec.name, rec.customer_r)))
            else:
                result.append((rec.id, '{}'.format(rec.name)))

        return result

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=50,  name_get_uid=None ):
        args = args or []
        domain = []

        if name:
            domain = ['|', ('email', operator, name), ('phone', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)






