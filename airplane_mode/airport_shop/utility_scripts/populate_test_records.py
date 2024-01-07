import frappe


def create_default_starter_records():
    # Create Tenant
    create_tenant_records()

    # Create Airport Area
    create_shop_area_records()

    # Create a Shop
    create_shop_records()

    print("Default starter records created successfully!")


def create_default_transaction_records():
    # Create a Shop Lease Contract
    create_lease_contract_records()

    # Create Payment Schedule
    create_payment_schedule_records()

    print("Default transaction records created successfully!")


def create_shop_records():
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "1",
            "area": "1A - Incheon International Airport",
            "available_for_lease": 1,
            "lease_fee_per_month": 15,
            "length_m": 15,
            "width_m": 10,
            "height_m": 5,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "2",
            "area": "1B - Incheon International Airport",
            "available_for_lease": 1,
            "lease_fee_per_month": 10,
            "length_m": 15,
            "width_m": 10,
            "height_m": 5,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "3",
            "area": "1C - Incheon International Airport",
            "available_for_lease": 1,
            "lease_fee_per_month": 20,
            "length_m": 15,
            "width_m": 10,
            "height_m": 5,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "4",
            "area": "1D - Incheon International Airport",
            "available_for_lease": 1,
            "lease_fee_per_month": 20,
            "length_m": 19,
            "width_m": 14,
            "height_m": 6,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "5",
            "area": "1A - Bandar Udara Internasional Soekarno Hatta",
            "available_for_lease": 1,
            "lease_fee_per_month": 10,
            "length_m": 25,
            "width_m": 18,
            "height_m": 7,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "6",
            "area": "1B - Bandar Udara Internasional Soekarno Hatta",
            "available_for_lease": 1,
            "lease_fee_per_month": 5,
            "length_m": 12,
            "width_m": 12,
            "height_m": 7,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "7",
            "area": "1C - Bandar Udara Internasional Soekarno Hatta",
            "available_for_lease": 1,
            "lease_fee_per_month": 15,
            "length_m": 25,
            "width_m": 20,
            "height_m": 7,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "8",
            "area": "1D - Bandar Udara Internasional Soekarno Hatta",
            "available_for_lease": 1,
            "lease_fee_per_month": 5,
            "length_m": 25,
            "width_m": 20,
            "height_m": 10,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "9",
            "area": "2B - Bandar Udara Internasional Soekarno Hatta",
            "available_for_lease": 0,
            "tenant": 16,
            "lease_fee_per_month": 15,
            "length_m": 15,
            "width_m": 20,
            "height_m": 4,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Dunkin Donuts",
            "number": "10",
            "area": "2C - Bandar Udara Internasional Soekarno Hatta",
            "available_for_lease": 0,
            "tenant": 16,
            "lease_fee_per_month": 20,
            "length_m": 18,
            "width_m": 8,
            "height_m": 4,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Starbucks",
            "number": "3",
            "area": "3B - Incheon International Airport",
            "available_for_lease": 0,
            "tenant": 18,
            "lease_fee_per_month": 55,
            "length_m": 35,
            "width_m": 40,
            "height_m": 5,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop",
            "shop_name": "Starbucks",
            "number": "4",
            "area": "2C - Incheon International Airport",
            "available_for_lease": 0,
            "tenant": 20,
            "lease_fee_per_month": 80,
            "length_m": 55,
            "width_m": 30,
            "height_m": 7,
        }
    ).insert()


def create_shop_area_records():
    # CGK Airport
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Bandar Udara Internasional Soekarno Hatta",
            "section": "A",
            "number": "2",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Bandar Udara Internasional Soekarno Hatta",
            "section": "A",
            "number": "3",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Bandar Udara Internasional Soekarno Hatta",
            "section": "B",
            "number": "1",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Bandar Udara Internasional Soekarno Hatta",
            "section": "B",
            "number": "3",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Bandar Udara Internasional Soekarno Hatta",
            "section": "C",
            "number": "1",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Bandar Udara Internasional Soekarno Hatta",
            "section": "C",
            "number": "2",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Bandar Udara Internasional Soekarno Hatta",
            "section": "D",
            "number": "1",
            "description": "Default shop area description",
        }
    ).insert()
    # ICN Airport
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Incheon International Airport",
            "section": "A",
            "number": "2",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Incheon International Airport",
            "section": "A",
            "number": "3",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Incheon International Airport",
            "section": "B",
            "number": "2",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Incheon International Airport",
            "section": "B",
            "number": "3",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Incheon International Airport",
            "section": "C",
            "number": "1",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Incheon International Airport",
            "section": "C",
            "number": "2",
            "description": "Default shop area description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Area",
            "airport": "Incheon International Airport",
            "section": "D",
            "number": "1",
            "description": "Default shop area description",
        }
    ).insert()


def create_tenant_records():
    frappe.get_doc(
        {
            "doctype": "Tenant",
            "tenant_name": "Tenant 1",
            "email": "riopramana@tobaconsulting.com",
            "description": "Default tenant description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Tenant",
            "tenant_name": "Tenant 2",
            "email": "riopramana@tobaconsulting.com",
            "description": "Default tenant description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Tenant",
            "tenant_name": "Tenant 3",
            "email": "riopramana@tobaconsulting.com",
            "description": "Default tenant description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Tenant",
            "tenant_name": "Tenant 4",
            "email": "riopramana@tobaconsulting.com",
            "description": "Default tenant description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Tenant",
            "tenant_name": "Tenant 5",
            "email": "riopramana@tobaconsulting.com",
            "description": "Default tenant description",
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Tenant",
            "tenant_name": "Tenant 6",
            "email": "riopramana@tobaconsulting.com",
            "description": "Default tenant description",
        }
    ).insert()


def create_lease_contract_records():
    frappe.get_doc(
        {
            "doctype": "Shop Lease Contract",
            "shop": "Dunkin Donuts - 9",
            "lease_duration": 12,
            "tenant": 16,
            "amount_owed": 180,
            "contract_signed_on": "2023-08-08",
            "contract_status": "Active",
            "docstatus": 1,
        }
    ).insert()
    frappe.get_doc(
        {
            "doctype": "Shop Lease Contract",
            "shop": "Dunkin Donuts - 10",
            "lease_duration": 6,
            "tenant": 16,
            "amount_owed": 120,
            "contract_signed_on": "2023-06-04",
            "contract_status": "Active",
            "docstatus": 1,
        }
    ).insert()

    # To test expired contract logic
    frappe.get_doc(
        {
            "doctype": "Shop Lease Contract",
            "shop": "Starbucks - 3",
            "lease_duration": 24,
            "tenant": 18,
            "amount_owed": 660,
            "contract_signed_on": "2020-10-09",
            "contract_status": "Active",
            "docstatus": 1,
        }
    ).insert()

    frappe.get_doc(
        {
            "doctype": "Shop Lease Contract",
            "shop": "Starbucks - 4",
            "lease_duration": 18,
            "tenant": 20,
            "amount_owed": 1440,
            "contract_signed_on": "2024-01-01",
            "contract_status": "Active",
            "docstatus": 1,
        }
    ).insert()


def create_payment_schedule_records():
    dunkin_9_contract = frappe.get_last_doc(
        "Shop Lease Contract",
        filters={"shop": "Dunkin Donuts - 9", "contract_status": "Active"},
    )
    frappe.get_doc(
        {
            "doctype": "Payment Schedule",
            "contract": dunkin_9_contract.name,
            "shop": "Dunkin Donuts - 9",
            "amount_due": 15,
            "due_on": "2023-09-08",
            "paid_on": "2023-09-09",
            "status": "Paid",
            "docstatus": 0,
        }
    ).insert().submit()
    frappe.get_doc(
        {
            "doctype": "Payment Schedule",
            "contract": dunkin_9_contract.name,
            "shop": "Dunkin Donuts - 9",
            "amount_due": 15,
            "due_on": "2023-10-08",
            "paid_on": "2023-10-09",
            "status": "Paid",
            "docstatus": 0,
        }
    ).insert().submit()
    frappe.get_doc(
        {
            "doctype": "Payment Schedule",
            "contract": dunkin_9_contract.name,
            "shop": "Dunkin Donuts - 9",
            "amount_due": 15,
            "due_on": "2023-11-08",
            "paid_on": "2023-11-09",
            "status": "Paid",
            "docstatus": 0,
        }
    ).insert().submit()
    # To test overdue logic
    frappe.get_doc(
        {
            "doctype": "Payment Schedule",
            "contract": dunkin_9_contract.name,
            "shop": "Dunkin Donuts - 9",
            "amount_due": 15,
            "due_on": "2023-12-08",
            "status": "Unpaid",
            "docstatus": 0,
        }
    ).insert()

    # To test creating monthly payment schedule automatically, don't create this doc
    # frappe.get_doc(
    #     {
    #         "doctype": "Payment Schedule",
    #         "contract": dunkin_9_contract.name,
    #         "shop": "Dunkin Donuts - 9",
    #         "amount_due": 15,
    #         "due_on": "2024-01-08",
    #         "status": "Unpaid",
    #     }
    # ).insert()
