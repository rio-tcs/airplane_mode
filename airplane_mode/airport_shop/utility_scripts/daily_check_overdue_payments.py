import frappe
from frappe.utils import today


def background_update_overdue_payment_schedules():
    frappe.enqueue(
        "airplane_mode.airport_shop.utility_scripts.daily_check_overdue_payments.update_overdue_payment_schedules"
    )


def update_overdue_payment_schedules():
    # Fetch all unpaid Payment Schedules where due_on is less than today and docstatus is 0 (Draft)
    payment_schedules = frappe.get_all(
        "Payment Schedule",
        filters={"due_on": ["<", today()], "status": "Unpaid", "docstatus": 0},
        fields=["name", "due_on", "status"],
    )

    # Iterate over each payment schedule and update the status to 'Overdue'
    for payment_schedule in payment_schedules:
        doc = frappe.get_doc("Payment Schedule", payment_schedule.name)
        doc.status = "Overdue"
        doc.save()
