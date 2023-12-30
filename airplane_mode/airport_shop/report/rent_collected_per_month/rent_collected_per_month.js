// Copyright (c) 2023, Rio Pramana and contributors
// For license information, please see license.txt

frappe.query_reports["Rent Collected per Month"] = {
    filters: [
        {
            fieldname: "from_date",
            label: __("From Date"),
            fieldtype: "Date",
            default: frappe.datetime.month_start(date),
            reqd: 1
        },
        {
            fieldname: "to_date",
            label: __("To Date"),
            fieldtype: "Date",
            default: frappe.datetime.month_end(date),
            reqd: 1
        },
        {
            fieldname: "tenant",
            label: __("Tenant"),
            fieldtype: "Link",
            options: "Tenant"
        },
        {
            fieldname: "shop",
            label: __("Shop"),
            fieldtype: "Link",
            options: "Shop"
        }
        // Add more filters if needed
    ]
}
