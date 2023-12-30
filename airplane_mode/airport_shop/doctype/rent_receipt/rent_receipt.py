# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import now


class RentReceipt(Document):
    pass


def create_rent_receipt(payment):
    new_receipt = frappe.new_doc("Rent Receipt")
    new_receipt.payment_id = payment.name
    new_receipt.date_issued = now()
    new_receipt.insert()
    return new_receipt.name
