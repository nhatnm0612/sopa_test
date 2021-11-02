from odoo import api, fields, models


class SopaProject(models.Model):
    _inherit = 'sopa.project'
    _description = 'Sopa Project'
    
    status = fields.Selection(
        selection=[("init", "New"), ("finish", "Finish"), ("fail", "Failed")],
        string="Status", required=True, default="init"
    )
    working_status = fields.Selection(
        selection=[("not_started", "Not Started"), ("active", "Active"), ("terminated", "Terminated")],
        string="Working Status", compute="_compute_working_status"
    )

    @api.depends("start_date", "due_date")
    def _compute_working_status(self):
        current_date = fields.Date.today()
        for r in self:
            if r.start_date and r.due_date:
                if current_date < r.start_date:
                    r.working_status = "not_started"
                elif r.start_date <= current_date <= r.due_date:
                    r.working_status = "active"
                elif current_date < r.due_date:
                    r.working_status = "terminated"
            r.working_status = "not_started"
