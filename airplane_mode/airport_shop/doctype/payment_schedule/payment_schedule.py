# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import add_months, today

from airplane_mode.airport_shop.doctype.rent_receipt.rent_receipt import (
    create_rent_receipt,
)


class PaymentSchedule(Document):
    def before_submit(self):
        self.status = "Paid"
        self.paid_on = today()
        self.receipt = create_rent_receipt(self)


def create_payment_schedule(contract, due_date):
    # Calculate the monthly payment amount
    monthly_amount_due = (
        contract.amount_owed / contract.lease_duration if contract.lease_duration else 0
    )
    # Create a new Payment Schedule for the next period
    new_schedule = frappe.new_doc("Payment Schedule")
    new_schedule.contract = contract.name
    new_schedule.shop = contract.shop
    new_schedule.due_on = due_date
    new_schedule.amount_due = monthly_amount_due
    new_schedule.status = "Unpaid"
    new_schedule.insert()


def create_next_payment_schedules():
    today_date = today()

    # Find all active shop lease contracts that are not yet expired
    active_contracts = frappe.get_all(
        "Shop Lease Contract",
        filters={"docstatus": 1, "lease_ends_on": [">", today_date]},
        fields=[
            "name",
            "shop",
            "contract_signed_on",
            "amount_owed",
            "lease_duration",
            "lease_ends_on",
        ],
    )

    for contract in active_contracts:
        # Check the date for the next payment schedule to be created
        # This will be based on the last payment schedule's due date
        last_payment_schedule = frappe.get_last_doc(
            "Payment Schedule",
            filters={"contract": contract.name},
            fields=["due_on"],
            order_by="due_on desc",
        )

        if last_payment_schedule:
            # Calculate the next due date
            next_due_date = add_months(last_payment_schedule.due_on, 1)
            if (
                (today_date >= last_payment_schedule.due_on)
                and (today_date < next_due_date)
                and (next_due_date <= contract.lease_ends_on)
            ):
                create_payment_schedule(contract, next_due_date)
