import frappe 

@frappe.whitelist()
def create_meeting_schedule(source_name, target_doc=None):
    from frappe.model.mapper import get_mapped_doc
    doclist = get_mapped_doc(
		"Opportunity",
		source_name,
		{
			"Opportunity": {
                "doctype": "Meeting Schedule",
                "field_map": {
					"opportunity_from":"party_type",					
				},
                
                
                },
			
		},
		target_doc,
	)
    return doclist

