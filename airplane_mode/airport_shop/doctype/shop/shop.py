# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Shop(Document):
    def validate(self):
        # Auto-set currency symbol from single doctype
        settings = frappe.get_single("Airport Shop Settings")
        self.currency_symbol = settings.default_currency

        if self.available_for_lease:
            if self.lease_fee_per_month <= 0:
                frappe.throw("Lease fee cannot be zero")

            if frappe.db.exists(
                {
                    "doctype": "Shop Lease Contract",
                    "shop": self.name,
                    "docstatus": 1,
                    "contract_status": "Active",
                }
            ):
                frappe.throw("An active contract for this Shop already exists")
        if self.length_m and self.width_m:
            self.area_m2 = self.length_m * self.width_m
