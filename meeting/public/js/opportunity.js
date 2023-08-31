frappe.ui.form.on('Opportunity', {
    refresh:function(frm){
        frm.add_custom_button(__('Meeting Schedule'), function () {
            frappe.model.open_mapped_doc({
                method: "meeting.api.create_meeting_schedule",
                frm: cur_frm
            })


        }, __('Create'));
    }
})