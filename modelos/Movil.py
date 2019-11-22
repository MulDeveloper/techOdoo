from odoo import models, fields, api

class Movil(models.Model):
	_name = 'tech.moviles'
	modelo = fields.Char('Modelo movil', required=True)
	marca = fields.Char('Marca', required=True)
	pulgadas = fields.Float('Pulgadas', required=True)
	precio = fields.Float('Precio', required=True)


@api.multi
def limpiar_campos(self):
	self.modelo = ""
	self.marca = ""
	self.pulgadas = ""
	self.precio = ""
	return True