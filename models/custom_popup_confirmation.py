# -*- coding: utf-8 -*-

from odoo import models, fields, _

class CustomPopupConfirmation(models.TransientModel):
    _name = 'paimon.custom.popup.confirmation'

    model = fields.Char()
    title = fields.Char()
    message = fields.Char()
    callback = fields.Char()

    def show(self, title, message, callback):
        popup = self.create(dict(
            title=title,
            message=message,
            callback=callback)
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