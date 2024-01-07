# Copyright (c) 2023, Rio Pramana and Contributors
# See license.txt

import frappe
from frappe.tests.utils import FrappeTestCase


class TestShopArea(FrappeTestCase):
    def test_before_save(self):
        # Create a test shop area
        shop_area = frappe.get_doc(
            {
                "doctype": "Shop Area",
                "number": 101,
                "section": "A",
                "airport": "Incheon International Airport",
            }
        )

        # Save the document, which should trigger before_save
        shop_area.save()

        # Check if code is set correctly
        expected_code = "101A"
        self.assertEqual(
            shop_area.code, expected_code, f"Code should be '{expected_code}'"
        )

    def tearDown(self):
        # Clean up to ensure each test is independent
        frappe.db.rollback()
