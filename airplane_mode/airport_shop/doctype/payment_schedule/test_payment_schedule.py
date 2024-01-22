# Copyright (c) 2023, Rio Pramana and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase
from frappe.utils import today


class TestPaymentSchedule(FrappeTestCase):
    def setUp(self):
        # Create a test shop lease contract
        self.contract = frappe.get_doc(
            {
                "doctype": "Shop Lease Contract",
                "shop": "Dunkin Donuts - 1",
                "tenant": "17",
                "lease_duration": 12,
                "amount_owed": 12000,
                "contract_signed_on": today(),
            }
        ).insert()

        self.contract.submit()

        self.payment_schedule = frappe.get_last_doc("Payment Schedule")

    def test_before_submit(self):
        # Submit the payment schedule
        self.payment_schedule.submit()

        # Reload to get updated values
        self.payment_schedule.reload()

        # Check if the status is now "Paid" and paid_on is set to today
        self.assertEqual(
            self.payment_schedule.status,
            "Paid",
            "Status should be 'Paid' after submission",
        )

        paid_on_str = self.payment_schedule.paid_on.strftime("%Y-%m-%d")
        self.assertEqual(
            paid_on_str,
            today(),
            "Paid on date should be set to today",
        )

        # Check if a receipt was created
        self.assertTrue(
            self.payment_schedule.receipt, "Receipt should be created upon submission"
        )

    def tearDown(self):
        # Clean up to ensure each test is independent
        frappe.db.rollback()


#  bench --site assignment.local run-tests --module airplane_mode.airport_shop.doctype.payment_schedule.test_payment_schedule  --test test_before_submit
