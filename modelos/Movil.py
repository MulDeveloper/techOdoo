from odoo import models, fields, api

class Movil(models.Model):
	_name = 'tech.moviles'
	modelo = fields.Char('Modelo movil', required=True)
    marca = fields.Char('Marca', required=True)
    pulgadas = fields.Float('Pulgadas', required=True)
    precio = fields.Float('Precio', required=True)


@api.one  
    def limpiar(self):
        self.modelo = ""
        return True

@api.multi
    def limpia_todo(self):
        done_recs = self.search([('modelo', '=', 'fender')])
        done_recs.write({'modelo': 'Fender'})
        return True