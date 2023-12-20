# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = [
        {"fieldtype": "Link", "label": "Airline", "fieldname": "airline", "width": 200, "options": "Airline"},
        {
            "fieldtype": "Currency",
            "label": "Revenue",
            "fieldname": "revenue",
            "width": 200,
        },
    ]
    data = (
        frappe.db.sql(
            """
        SELECT
            al.name as airline_name,
            sum(at.total_amount) as total_revenue
        FROM
            `tabAirplane Ticket` at
            JOIN `tabAirplane Flight` af ON at.flight = af.name
            JOIN `tabAirplane` ap ON af.airplane = ap.name
            RIGHT JOIN `tabAirline` al ON ap.airline = al.name
        GROUP BY
            al.name
        ORDER BY
            total_revenue desc
        """
        ),
    )[0]
    chart = {
        "type": "donut",
        "data": {
            "labels": [row[0] for row in data],
            "datasets": [{"values": [row[1] for row in data]}],
        },
    }
    total_revenue = sum((row[1] if row[1] else 0) for row in data)
    report_summary = [
        {
            "value": total_revenue,
            "indicator": "green" if total_revenue > 0 else "red",
            "label": "Total Revenue",
            "datatype": "Currency",
        }
    ]

    return columns, data, None, chart, report_summary
