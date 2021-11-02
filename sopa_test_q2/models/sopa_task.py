from odoo import api, fields, models


class SopaTask(models.Model):
    _inherit = 'sopa.task'
    _description = 'Sopa Task'
    
    status = fields.Selection(
        selection=[("init", "New"), ("in_progress", "In Progress"), ("finish", "Finished")],
        string="Status", required=True, default="init"
    )
    working_status = fields.Selection(
        selection=[("not_start", "Not Start"), ("in_working_time", "In Working Time"), ("finish", "Finished"), ("over_deadline", "Overdue")],
        string="Working Status", compute="_compute_working_status"
    )

    @api.depends("status", "start_date", "due_date")
    def _compute_working_status(self):
        current_date = fields.Date.today()
        for r in self:
            if r.status == "finish":
                r.working_status = "finish"
            elif r.start_date and r.due_date:
                if current_date < r.start_date:
                    r.working_status = "not_start"
                elif r.start_date <= current_date <= r.due_date:
                    r.working_status = "in_working_time"
                elif r.due_date < current_date:
                    r.working_status = "over_deadline"
            r.working_status = "not_start"
