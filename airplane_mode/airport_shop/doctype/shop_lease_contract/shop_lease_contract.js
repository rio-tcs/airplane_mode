// Copyright (c) 2023, Rio Pramana and contributors
// For license information, please see license.txt

frappe.ui.form.on("Shop Lease Contract", {
	refresh(frm) {
        frm.set_query("shop", ()=>{
            return {
                filters: {
                    "available_for_lease": 1
                }
            }
        })
	},
});
