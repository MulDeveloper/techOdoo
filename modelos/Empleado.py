from odoo import models, fields, api

class Empleado(models.Model):
	_name = 'tech.empleados'
	cod = fields.Integer('Cod empleado', required=True)
	nombre = fields.Char('Nombre empleado', required=True)
    apellido = fields.Char('Apellido empleado', required=True)
    puesto = fields.Char('Puesto empleado', required=True)
    sueldo = fields.Float('Sueldo', required=True)
    
