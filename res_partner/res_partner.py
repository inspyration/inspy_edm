# -*- coding: utf-8 -*-
##############################################################################
#
#    EDM, module for Odoo, Open Source Management Solution
#    Copyright (C) 2014 InsPyration EURL (<http://www.inspyration.fr>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

__author__ = "Sébastien CHAZALLET & Alicia FLOREZ"
__copyright__ = "Copyright 2014"
__credits__ = ["Sébastien CHAZALLET", "Alicia FLOREZ", "www.insPyration.fr", "www.formation-python.com"]
__license__ = "AGPL"
__version__ = "1.0"
__maintainer__ = "Alicia FLOREZ"
__email__ = "contact@inspyration.fr"
__status__ = "Production"

from openerp.osv import fields,osv

class res_partner(osv.osv):
    _inherit = 'res.partner'

    def _edm_docs_count(self, cr, uid, ids, field_name, arg, context=None):
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            res[partner.id] = len(partner.document_ids)
        return res

    _columns = {
        'document_ids': fields.one2many(
            'inspy.edm.doc',
            'partner_id',
            string="Documents",
        ),
        'edm_docs_count': fields.function(
            _edm_docs_count,
            string="Documents",
            type='integer',
        ),
    }