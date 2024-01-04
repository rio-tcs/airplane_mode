# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Shop(Document):
    def validate(self):
        if self.available_for_lease:
            if self.lease_fee_per_month <= 0:
                frappe.throw("Lease fee cannot be zero")

            if frappe.db.exists(
                {"doctype": "Shop Lease Contract", "shop": self.name, "docstatus": 1}
            ):
                frappe.throw("An active contract for this Shop already exists")
        if self.length and self.width:
            self.area_m2 = self.length * self.width
