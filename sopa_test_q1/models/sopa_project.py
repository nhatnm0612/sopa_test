from odoo import _, api, fields, models


class SopaProject(models.Model):
    _name = "sopa.project"
    _description = "Sopa Project"
    
    name = fields.Char(
        string="Name", required=True,
        help="Project Name"
    )
    manager_user_id = fields.Many2one(
        comodel_name="res.users", string="Manager", required=True,
        domain="[('share', '=', False)]", help="Manager of Project"
    )
    start_date = fields.Date(
        string="Start Date", default=fields.Date.today(), required=True
    )
    due_date = fields.Date(
        string="Due Date"
    )
    task_ids = fields.One2many(
        comodel_name="sopa.task", inverse_name="project_id", string="Tasks"
    )
