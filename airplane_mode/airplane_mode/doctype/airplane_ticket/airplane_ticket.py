# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class AirplaneTicket(Document):
    def before_save(self):
        self.total_amount = float(self.flight_price) + sum(
            item.amount for item in self.add_ons
        )

    def validate(self):
        flight = frappe.get_doc("Airplane Flight", self.flight)
        airplane = frappe.get_doc("Airplane", flight.airplane)
        num_of_tix = frappe.db.count("Airplane Ticket", filters={"flight": self.flight})
        if num_of_tix < airplane.capacity:
            # Logic to remove duplicate add-ons
            unique_add_ons = {}
            for add_on in self.add_ons:
                if add_on.item not in unique_add_ons:
                    unique_add_ons[add_on.item] = add_on
                else:
                    frappe.msgprint(f"Duplicate add-on '{add_on.item}' removed.")

            # Update the add_ons table with only unique entries
            self.set("add_ons", list(unique_add_ons.values()))
        else:
            frappe.throw(
                "Unable to create new ticket: This flight has been fully booked"
            )

    def on_submit(self):
        if not self.status == "Boarded":
            frappe.throw("Can't be submitted if the status is not Boarded!")

    def before_insert(self):
        import random

        random_int = random.randint(1, 99)
        random_alphabet = random.choice(["A", "B", "C", "D", "E"])
        random_seat = str(random_int) + random_alphabet

        self.seat = random_seat
