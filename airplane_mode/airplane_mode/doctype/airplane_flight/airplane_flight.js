// Copyright (c) 2023, Rio Pramana and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Flight", {
	refresh(frm) {
        frm.add_custom_button("Assign Gate Number", () =>{
            frappe.prompt({
                fieldname: 'gate_number',
                label: 'Gate Number',
                fieldtype: 'Data',
                reqd: 1,
            }, (data)=>{
                frm.set_value('gate_number', data.gate_number);
                frm.save();
            })
        }, 'Actions');
	},
});
