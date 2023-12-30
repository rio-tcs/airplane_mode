import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    return columns, data


def get_columns():
    return [
        {"fieldname": "month", "label": "Month", "fieldtype": "Data", "width": 100},
        {
            "fieldname": "total_payments",
            "label": "Total Payments Received",
            "fieldtype": "Currency",
            "width": 120,
        },
        {
            "fieldname": "payments_count",
            "label": "Payments Count",
            "fieldtype": "Int",
            "width": 120,
        },
        {
            "fieldname": "outstanding_payments",
            "label": "Outstanding Payments",
            "fieldtype": "Currency",
            "width": 120,
        },
    ]


def get_data(filters):
    conditions = get_conditions(filters)

    query = """
        SELECT
            DATE_FORMAT(ps.due_on, '%M %Y') as month,
            SUM(ps.amount_due) as total_payments,
            COUNT(ps.name) as payments_count,
            SUM(
                CASE
                    WHEN ps.status = 'Unpaid' THEN ps.amount_due
                    ELSE 0
                END
            ) as outstanding_payments
        FROM 
            `tabPayment Schedule` as ps
        {where_conditions}
        GROUP BY 
            DATE_FORMAT(ps.due_on, '%M %Y')
        ORDER BY 
            MIN(ps.due_on)
    """.format(
        where_conditions=conditions
    )

    return frappe.db.sql(query, as_dict=1)


def get_conditions(filters):
    conditions = "WHERE ps.docstatus = 1"
    if filters:
        if filters.get("from_date"):
            conditions += " AND ps.due_on >= %(from_date)s"
        if filters.get("to_date"):
            conditions += " AND ps.due_on <= %(to_date)s"
    return conditions
