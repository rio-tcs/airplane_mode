import frappe
from frappe.utils import formatdate


def background_send_rent_reminders():
    frappe.enqueue(
        "airplane_mode.airport_shop.utility_scripts.send_monthly_rent_reminder.send_rent_reminders"
    )


def send_rent_reminders():
    rent_due_query = """
        SELECT
            s.tenant,
            t.email,
            t.tenant_name,
            s.name as shop,
            ps.due_on as due_date,
            ps.status
        FROM
            `tabPayment Schedule` ps
        JOIN
            `tabShop` s ON ps.shop = s.name
        JOIN
            `tabTenant` t ON s.tenant = t.name
        WHERE
            ps.docstatus = 0 AND
            ps.status NOT IN ('Paid', 'Voided')
        ORDER BY
            s.tenant, s.name, ps.due_on DESC
    """

    tenants_due_for_rent = frappe.db.sql(rent_due_query, as_dict=True)

    grouped_data = {}
    for data in tenants_due_for_rent:
        tenant_key = data.tenant
        if tenant_key not in grouped_data:
            grouped_data[tenant_key] = {
                "tenant_name": data.tenant_name,
                "email": data.email,
                "shops": [],
            }
        grouped_data[tenant_key]["shops"].append(
            {
                "shop": data.shop,
                "due_date": data.due_date,
                "status": data.status,
            }
        )

    for tenant in grouped_data.values():
        send_rent_due_email(tenant)


def send_rent_due_email(tenant_info):
    rent_details = "".join(
        f"<li>Shop {shop_info['shop']}: due on {formatdate(shop_info['due_date'])} (Status: {shop_info['status']})</li>"
        for shop_info in tenant_info["shops"]
    )

    tenant_name = tenant_info.get(
        "tenant_name", "Tenant"
    )  # Fallback to "Tenant" if name is not available
    subject = "Upcoming Rent Due Reminder"
    message = f"""
        <p>Dear {tenant_name},</p>
        <p>This is a friendly reminder that rent for your leased shop(s) is due soon:</p>
        <ul>
            {rent_details}
        </ul>
        <p>Please ensure that payment is made by the due date to avoid any late fees.</p>
        <p>Thank you for your attention to this matter.</p>
        <p>Best regards,<br>Your Management Team</p>
    """

    frappe.sendmail(
        recipients=tenant_info["email"], subject=subject, message=message, now=True
    )


# def send_test_email(recipient_email, subject, message):
#     from frappe import log_error, sendmail

#     try:
#         sendmail(recipients=recipient_email, subject=subject, message=message)
#         frappe.db.commit()  # Ensure that the Email Queue is committed
#         print(f"Test email has been sent to {recipient_email}")
#     except Exception as e:
#         error_message = str(e)
#         log_error(title="Email Sending Failed", message=error_message)
#         print(f"An error occurred while sending the email: {error_message}")


# def test_email():
#     # Set the recipient's email, subject, and message
#     test_recipient = "riopramana@tobaconsulting.com"
#     test_subject = "Test Email from Frappe"
#     test_message = "This is a test email sent from the Frappe framework to verify email functionality."

#     # Send the test email
#     send_test_email(test_recipient, test_subject, test_message)
