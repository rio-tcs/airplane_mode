# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

from datetime import date, datetime

# import frappe
from frappe.model.document import Document


class Tenant(Document):
    def before_save(self):
        if self.date_of_birth:
            today = date.today()
            dob = datetime.strptime(self.date_of_birth, "%Y-%m-%d").date()
            self.age = (
                today.year
                - dob.year
                - ((today.month, today.day) < (dob.month, dob.day))
            )
