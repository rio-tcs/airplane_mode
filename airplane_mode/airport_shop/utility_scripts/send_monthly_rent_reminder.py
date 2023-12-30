import frappe
from frappe.utils import formatdate


def send_rent_reminders():
    rent_due_query = """
        SELECT
            s.tenant,
            t.email,
            GROUP_CONCAT(DISTINCT s.name ORDER BY ps.due_on ASC) as shops,
            GROUP_CONCAT(DISTINCT ps.due_on ORDER BY ps.due_on ASC) as due_dates
        FROM
            `tabPayment Schedule` ps
        INNER JOIN
            `tabShop` s ON ps.shop = s.name
        INNER JOIN
            `tabTenant` t ON s.tenant = t.name
        WHERE
            ps.docstatus = 1 AND
            ps.status NOT IN ('Paid', 'Voided')
        GROUP BY
            s.tenant
    """

    tenants_due_for_rent = frappe.db.sql(rent_due_query, as_dict=True)

    for tenant in tenants_due_for_rent:
        send_rent_due_email(tenant)


def send_rent_due_email(tenant_info):
    shops_due = zip(
        tenant_info["shops"].split(","), tenant_info["due_dates"].split(",")
    )
    rent_details = "".join(
        f"<li>Shop {shop}: due on {formatdate(due_date)}</li>"
        for shop, due_date in shops_due
    )

    subject = "Upcoming Rent Due Reminder"
    message = f"""
        <p>Dear Tenant,</p>
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


def send_test_email(recipient_email, subject, message):
    from frappe import log_error, sendmail

    try:
        sendmail(recipients=recipient_email, subject=subject, message=message)
        frappe.db.commit()  # Ensure that the Email Queue is committed
        print(f"Test email has been sent to {recipient_email}")
    except Exception as e:
        error_message = str(e)
        log_error(title="Email Sending Failed", message=error_message)
        print(f"An error occurred while sending the email: {error_message}")


def test_email():
    # Set the recipient's email, subject, and message
    test_recipient = (
        "riopramana@tobaconsulting.com"  # Replace with an actual email address
    )
    test_subject = "Test Email from Frappe"
    test_message = "This is a test email sent from the Frappe framework to verify email functionality."

    # Send the test email and log errors if any
    send_test_email(test_recipient, test_subject, test_message)
