# Copyright (c) 2023, Rio Pramana and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
    columns = [
        {"fieldtype": "Data", "label": "Airline", "fieldname": "airline"},
        {"fieldtype": "Currency", "label": "Revenue", "fieldname": "revenue"},
    ]
    data = []

    return columns, data
