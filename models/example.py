from odoo import models, fields

class Example(models.Model):
    """
    this model is not include in __init__.py, 
    so don't worry because this model will not affect on your current project and database
    """
    _name = 'example'

    state = fields.Selection(
        [('draft', 'Draft'), ('done', 'Doned')])
    
    def action_done(self):
        self.write(dict(state='done'))

    def open_confirmation_action_done(self):
        """
        Example show confirmation popup before actual call function action_done.
        """
        popup = self.env['paimon.popup.confirmation']
        action = popup.show(self, 'Are you sure to set to done state?', 'action_done')
        return action

    def open_confirmation_action_done_chaining(self):
        """
        Example show double confirmation popup before actual call function action_done.
        """
        popup = self.env['paimon.popup.confirmation']
        action = popup.show(self, 'Are you sure to this action?', 'open_confirmation_action_done')
        return action
