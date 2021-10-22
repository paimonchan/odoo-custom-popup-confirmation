# -*- coding: utf-8 -*-

from odoo import models, fields, _

# TODO: add example how to used this custom popup
class CustomPopupConfirmation(models.TransientModel):
    _name = 'paimon.custom.popup.confirmation'

    message = fields.Char()
    callback = fields.Char()
    source_model = fields.Char()

    def show(self, records, message, callback_name):
        context = dict(self.env.context)
        context.update(record_ids=records.ids)

        popup = self.create(dict(
            message=message,
            callback=callback_name,
            source_model=records._model,)
        )

        action =  dict(
            target = 'new',
            res_id=popup.id,
            view_mode = 'form',
            name = _(self.title),
            res_model = self._name,
            type = 'ir.actions.act_window',
            context = dict(self.env.context),
        )
        return action