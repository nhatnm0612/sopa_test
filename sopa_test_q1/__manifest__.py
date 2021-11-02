{
    "name": "SoPa Odoo Test Question 1",
    "version": "15.0.0.1.0",
    "description": "Create module project-base",
    "summary": "Create module project-base",
    "author": "NhatNM0612",
    "website": "https://github.com/nhatnm0612",
    "license": "OPL-1",
    "category": "",
    "depends": [
        "base"
    ],
    "data": [
        # SECURITY
        "security/ir.model.access.csv",
        # VIEWS
        "views/sopa_project_views.xml",
        "views/sopa_task_views.xml",
        "views/sopa_menuitem_views.xml",
    ],
    "demo": [
        "demo/sopa_test_q1_demo.xml",
    ],
    "auto_install": False,
    "application": False,
}
