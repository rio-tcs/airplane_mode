# Copyright (c) 2024, Rio Pramana and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    chart = get_chart(data)
    report_summary = get_report_summary(data)
    return columns, data, "Shops per Airport Pie Chart", chart, report_summary


def get_columns():
    return [
        {
            "fieldname": "airport_name",
            "label": "Airport",
            "fieldtype": "Link",
            "options": "Airport",
            "width": 300,
        },
        {
            "fieldname": "total_shops",
            "label": "Total Shops",
            "fieldtype": "Int",
            "width": 150,
        },
    ]


def get_data(filters):
    query = """
        SELECT
			count(ts.name) AS total_shops,
			ta.name AS airport_name
		FROM
			`tabShop` ts
		JOIN
			`tabShop Area` tsa ON ts.area = tsa.name
		JOIN
			`tabAirport` ta ON ta.name = tsa.airport
		GROUP BY
			ta.name
    """

    return frappe.db.sql(query, as_dict=1)


def get_chart(data):
    return {
        "type": "pie",
        "data": {
            "labels": [row.airport_name for row in data],
            "datasets": [{"values": [row.total_shops for row in data]}],
        },
    }


def get_report_summary(data):
    total_shops = sum(row.total_shops for row in data)
    report_summary = [
        {
            "value": len(data),
            "label": "Total Airport Involved",
            "datatype": "Int",
        },
        {
            "value": total_shops,
            "label": "Total Shops",
            "datatype": "Int",
        },
    ]
    return report_summary
