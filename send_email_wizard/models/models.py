# -*- encoding: utf-8 -*-
from odoo import models, fields, api

class res_partner(models.Model):
    _inherit = 'res.partner'

    def action_send_email(self):
        '''
        Esta función abre una ventana para escribir un email, con la plantilla por defecto.
        '''
   
        self.ensure_one()
        ir_model_data = self.env['ir.model.data']
        try:
            template_id = \
            ir_model_data.get_object_reference('send_email_wizard', 'email_template')[1]
        except ValueError:
            template_id = False
        try:
            compose_form_id = ir_model_data.get_object_reference('mail', 'email_compose_message_wizard_form')[1]
        except ValueError:
            compose_form_id = False
        ctx = {
                   'default_model': 'res.partner',
                   'default_res_id': self.ids[0],
                   'default_use_template': bool(template_id),
                   'default_template_id': template_id,
                   'default_composition_mode': 'comment',
        }
        return {
                   'name': ('Compose Email'),
                   'type': 'ir.actions.act_window',
                   'view_mode': 'form',
                   'res_model': 'mail.compose.message',
                   'views': [(compose_form_id, 'form')],
                   'view_id': compose_form_id,
                   'target': 'new',
                   'context': ctx,
        }