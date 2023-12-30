# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_months, today

from airplane_mode.airport_shop.doctype.payment_schedule.payment_schedule import (
    create_payment_schedule,
)


class ShopLeaseContract(Document):
    def before_submit(self):
        self.contract_signed_on = today()
        self.lease_ends_on = add_months(self.contract_signed_on, self.lease_duration)
        shop = frappe.get_doc("Shop", self.shop)
        shop.available_for_lease = 0
        shop.tenant = self.tenant
        shop.save()

    def before_save(self):
        shop = frappe.get_doc("Shop", self.shop)
        amount_owed = shop.lease_fee_per_month * self.lease_duration
        self.amount_owed = amount_owed

    def validate(self):
        if self.lease_duration <= 0:
            frappe.throw("Lease duration must be at least 1 month")
        if frappe.db.exists(
            {"doctype": "Shop Lease Contract", "shop": self.shop, "docstatus": 1}
        ):
            frappe.throw("An active contract for this Shop already exists")

    def on_submit(self):
        create_payment_schedule(self, add_months(self.contract_signed_on, 1))
