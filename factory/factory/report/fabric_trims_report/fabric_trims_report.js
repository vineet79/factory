frappe.query_reports["Fabric Trims Report"] = {
    "filters": [
        {
            "fieldname":"project",
            "label": __("Project"),
            "fieldtype": "Link",
            "options": "Project",
	    "reqd": 1
        },{
            "fieldname":"supplier",
            "label": __("Supplier"),
            "fieldtype": "Link",
            "name": "supplier",
            "options": "Supplier",
            "reqd": 1
        },
    ]
}
