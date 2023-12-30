// Copyright (c) 2023, Rio Pramana and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop", {
	refresh(frm) {
        if(!frm.is_new()){
            frm.add_custom_button(('Make Contract'), function(){
                frappe.new_doc('Shop Lease Contract', {
                    shop: frm.doc.name,
                    area: frm.doc.area
                });
            });
        }
	},
});
