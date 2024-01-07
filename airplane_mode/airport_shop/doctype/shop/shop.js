// Copyright (c) 2023, Rio Pramana and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop", {
	refresh(frm) {
        if(!frm.is_new()){
            frm.add_custom_button(('Make Contract'), function(){
                frappe.call({
                    method: "airplane_mode.airport_shop.doctype.shop_lease_contract.shop_lease_contract.validate_active_contract",
                    args: {shop: frm.doc.name},
                    freeze: true,
                    freeze_message: ("Running checks..."),
                    callback: function(r){
                        if (!r.exc){
                            // If no exception was thrown, no active contract exists
                            // Proceed to create a new one
                            frappe.new_doc('Shop Lease Contract', {
                                shop: frm.doc.name,
                                area: frm.doc.area
                            });
                        }
                    }
                });
            });
        }
	},
});
