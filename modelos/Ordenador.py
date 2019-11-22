from odoo import models, fields, api

class Ordenador(models.Model):
	_name = 'tech.ordenadores'
	modelo = fields.Char('Modelo ordenador', required=True)
    marca = fields.Char('Marca ordenador', required=True)
    pulgadas = fields.Float('Pulgadas', required=True)
    precio = fields.Float('Precio', required=True)
    procesador = fields.Char('Procesador', required=True)
    ram = fields.Integer('RAM', required=True)
    discoDuro = fields.Integer('Disco duro', required=True)
