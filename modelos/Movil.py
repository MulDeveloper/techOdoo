from odoo import models, fields, api

class Movil(models.Model):
	_name = 'tech.moviles'
	modelo = fields.Char('Modelo movil', required=True)
	cantidad = fields.Integer('Cantidad terminales', required=True)
	marca = fields.Char('Marca', required=True)
	pulgadas = fields.Float('Pulgadas', required=True)
	precio = fields.Float('Precio', required=True)
	iva = fields.Float('IVA', required=True)
	total = fields.Float(string='Total', compute='calculoTotal')


	@api.one
	@api.depends('precio', 'cantidad', 'iva')
	def calculoTotal(self):
		aux = (self.precio * self.cantidad) 
		self.total = aux + (aux * (self.iva/100))