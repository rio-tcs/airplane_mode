import frappe


def update_overdue_payment_schedules():
    # Fetch all unpaid Payment Schedules where due_on is less than today and docstatus is 0 (Draft)
    payment_schedules = frappe.get_all(
        "Payment Schedule",
        filters={"due_on": ["<", "today"], "status": "Unpaid", "docstatus": 0},  # Draft
        fields=["name", "due_on", "status"],
    )

    # Iterate over each payment schedule and update the status to 'Overdue'
    for payment_schedule in payment_schedules:
        doc = frappe.get_doc("Payment Schedule", payment_schedule.name)
        doc.status = "Overdue"
        doc.save()
        # frappe.db.commit()  # Commit changes to the database
