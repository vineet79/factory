frappe.query_reports["Fabric Balance Report"] = {
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
cur_frm.fields_dict['supplier'].get_query = function(doc, cdt, cdn) {
	return{
		filters: {'supplier_type': 'Garment Jobworker'}
	}
}
