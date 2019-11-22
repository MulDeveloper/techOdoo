from odoo import models, fields, api

class Aplicacion(models.Model):
	_name = 'tech.aplicaciones'
	nombre = fields.Char('Nombre app', required=True)
    cliente = fields.Char('Cliente app', required=True)
    tipoApp = fields.Char('Tipo app', required=True)
    costeDesarrollo = fields.Float('Coste desarrollo', required=True)
