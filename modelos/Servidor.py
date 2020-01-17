from odoo import models, fields, api

class Servidor(models.Model):
	_name = 'tech.servidores'
	modelo = fields.Char('Modelo servidor', required=True)
	marca = fields.Char('Marca servidor', required=True)
	tipoServidor = fields.Char('Tipo', required=True)
	precioAlquiler = fields.Float('Precio alquiler', required=True)
	procesadores = fields.Char('Procesadores', required=True)
	ram = fields.Integer('RAM', required=True)
	discosDuros = fields.Integer('Numero discos duros', required=True)


