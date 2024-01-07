# Copyright (c) 2023, Rio Pramana and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestShopLeaseContract(FrappeTestCase):
    def setUp(self):
        # Create a test shop lease contract
        self.contract = frappe.get_doc(
            {
                "doctype": "Shop Lease Contract",
                "shop": "_Test Shop",
                "tenant": "Test Tenant",
                "lease_duration": 12,  # 12 months
            }
        ).insert()

    def test_before_cancel(self):
        # Submit the contract to make it cancellable
        self.contract.submit()

        # Cancel the contract, which should trigger before_cancel
        self.contract.cancel()

        # Reload to get updated values
        self.contract.reload()

        # Check if the contract status is now "Voided"
        self.assertEqual(
            self.contract.status,
            "Voided",
            "Contract status should be 'Voided' after cancellation",
        )

    def tearDown(self):
        # Clean up to ensure each test is independent
        frappe.db.rollback()
        frappe.db.rollback()
