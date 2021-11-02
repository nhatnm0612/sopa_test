from odoo import _, api, fields, models


class SopaTask(models.Model):
    _name = "sopa.task"
    _description = "Sopa Task"
    
    name = fields.Char(
        string="Name", required=True
    )
    user_id = fields.Many2one(
        comodel_name="res.users", string="User In Charge", domain="[('share', '=', False)]"
    )
    start_date = fields.Datetime(
        string="Start Date", default=fields.Datetime.now()
    )
    due_date = fields.Datetime(
        string="End Date", help="End Date of Task"
    )
    project_id = fields.Many2one(
        comodel_name="sopa.project", string="Project", required=True
    )

    _sql_constraints = [
        ("project_task_name_uniq", "UNIQUE(name, project_id)", "It shouldn't have 2 tasks with the same name in 1 project!")
    ]
