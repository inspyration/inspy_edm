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

import openerp
from openerp.osv import fields, osv
from datetime import timedelta, datetime


#==============================================================================#
#                              class document                                  #
#==============================================================================#
class Document(osv.Model):
    
    _name = 'inspy.edm.doc'
    _description = "Document"
    
    _columns = {
        'name': fields.char(
            'Title',
            size=256,
            required=True,
            select=True,
        ),
        'description': fields.text(
            string="Description",
        ),
        'type_id': fields.many2one(
            'semantics.signifier',
            required=True,
            string="Type",
            domain=[('field_id.name','=',"Partner's documents types")],
        ),
        'content': fields.binary(
            string="Content",
        ),
        'content_filename': fields.char(
            'Content filename',
            size=256,
            select=True,
        ),
        'additional_information': fields.text(
            string="Additional information",
        ),
        'partner_id': fields.many2one(
            'res.partner',
            required=True,
            string="Partner",
        ),
        'tag_ids': fields.many2many(
            'semantics.signifier',
            'inspy_doc_tag_rel',
            'tag_id',
            'doc_id',
            string="Tags",
            domain=[('field_id.name','=',"Partner's documents key words")],
        ),
    }
    
#==============================================================================#
#                                 class type                                   #
#==============================================================================#
class Type(osv.Model):
    
    _name = 'inspy.edm.type'
    _description = "Document"
    
    _columns = { 
        'name': fields.char(
            'Title',
            size=256,
            required=True,
            select=True,
        ),
    }