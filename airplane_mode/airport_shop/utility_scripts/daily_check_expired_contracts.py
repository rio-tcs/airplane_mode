import frappe
from frappe.utils import today


def update_expired_contracts():
    # Fetch all active contracts where lease_ends_on is less than today
    contracts = frappe.get_all(
        "Shop Lease Contract",
        filters={"lease_ends_on": ["<", today()], "contract_status": "Active"},
    )

    for contract in contracts:
        doc = frappe.get_doc("Shop Lease Contract", contract.name)
        doc.contract_status = "Expired"
        doc.save()
        update_expired_contract_shop(doc.shop)


def update_expired_contract_shop(shop_name):
    shop = frappe.get_doc("Shop", shop_name)
    shop.tenant = ""
    shop.available_for_lease = 1
    shop.save()
