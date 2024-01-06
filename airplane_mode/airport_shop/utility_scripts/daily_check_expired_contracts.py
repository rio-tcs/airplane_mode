import frappe


def update_expired_contracts():
    # Fetch all active contracts where lease_ends_on is less than today
    contracts = frappe.get_all(
        "Shop Lease Contract",
        filters={"lease_ends_on": ["<", "today"], "status": "Active"},
    )

    for contract in contracts:
        doc = frappe.get_doc("Shop Lease Contract", contract.name)
        doc.status = "Expired"
        doc.save()
        frappe.db.commit()  # Commit changes to the database
        update_expired_contract_shop(doc.shop)


def update_expired_contract_shop(shop_name):
    shop = frappe.get_doc(shop_name)
    shop.tenant = ""
    shop.available_for_lease = 1
    shop.save()
    frappe.db.commit()
