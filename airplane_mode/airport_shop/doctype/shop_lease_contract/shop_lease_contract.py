# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_months

from airplane_mode.airport_shop.doctype.payment_schedule.payment_schedule import (
    create_payment_schedule,
)


class ShopLeaseContract(Document):
    def before_submit(self):
        self.contract_signed_on = today()
        self.lease_ends_on = add_months(self.contract_signed_on, self.lease_duration)
        self.contract_status = "Active"
        shop = frappe.get_doc("Shop", self.shop)
        shop.available_for_lease = 0
        shop.tenant = self.tenant
        shop.save()

    def before_cancel(self):
        self.contract_status = "Voided"

    def on_cancel(self):
        shop = frappe.get_doc("Shop", self.shop)
        shop.available_for_lease = 1
        shop.tenant = ""
        shop.save()

    def before_save(self):
        shop = frappe.get_doc("Shop", self.shop)
        amount_owed = shop.lease_fee_per_month * self.lease_duration
        self.amount_owed = amount_owed

    def validate(self):
        validate_active_contract(self.shop)
        settings = frappe.get_single("Airport Shop Settings")
        max_shops_allowed = settings.maximum_shops_per_tenant
        active_contracts = frappe.db.count(
            "Shop Lease Contract",
            {
                "tenant": self.tenant,
                "docstatus": 1,  # Document status 1 means the document is submitted
                "lease_ends_on": [
                    ">",
                    "today",
                ],  # Assuming there is an end_date field to indicate active contracts
            },
        )
        if active_contracts >= max_shops_allowed:
            frappe.throw(
                f"The tenant has already leased the maximum allowed number of shops ({max_shops_allowed})."
            )
        if self.lease_duration < settings.minimum_lease_duration_months:
            frappe.throw(
                f"Lease duration must be at least {settings.minimum_lease_duration_months} months"
            )
        elif self.lease_duration > settings.maximum_lease_duration_months:
            frappe.throw(
                f"The maximum lease duration is {settings.maximum_lease_duration_months} months"
            )

        # Auto-set currency symbol from single doctype
        settings = frappe.get_single("Airport Shop Settings")
        self.currency_symbol = settings.default_currency

    def on_submit(self):
        create_payment_schedule(self, add_months(self.contract_signed_on, 1))


@frappe.whitelist()
def validate_active_contract(shop):
    """Check if there is an active contract for the shop"""
    if frappe.db.exists(
        {
            "doctype": "Shop Lease Contract",
            "shop": shop,
            "docstatus": 1,
            "contract_status": "Active",
        }
    ):
        frappe.throw("An active contract for this Shop already exists")
