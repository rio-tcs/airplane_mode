# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe
from frappe.website.website_generator import WebsiteGenerator


class AirplaneFlight(WebsiteGenerator):
    def on_submit(self):
        if not self.gate_number:
            frappe.throw("A gate number must be assigned before submitting")
        self.status = "Completed"
        # update every ticket's gate number
        tickets = frappe.get_all(
            "Airplane Ticket",
            filters={"flight": self.name},
            fields=["name", "gate_number"],
        )
        for ticket in tickets:
            ticket_doc = frappe.get_doc("Airplane Ticket", ticket.name)
            ticket_doc.gate_number = self.gate_number
            ticket_doc.save()

        frappe.db.commit()
