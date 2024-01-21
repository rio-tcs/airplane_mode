// Copyright (c) 2024, Rio Pramana and contributors
// For license information, please see license.txt

frappe.query_reports["Shops per Airport"] = {
	"filters": [
		{
			"fieldtype": "Data",
			"fieldname": "airport_country_filter",
			"label": "Country",
		}
	],
	onload(report) {
        report.page.add_button('See Available Shops', function() {
            window.open('/available-shops');
        });
    }
};
