// Copyright (c) 2023, Rio Pramana and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
        frm.add_custom_button("Assign Seat", () =>{
            frappe.prompt({
                fieldname: 'seat_number',
                label: 'Seat Number',
                fieldtype: 'Data',
                reqd: 1,
            }, (data)=>{
                frm.set_value('seat', data.seat_number);
                frm.save();
            })
        }, 'Actions');
	},
});
