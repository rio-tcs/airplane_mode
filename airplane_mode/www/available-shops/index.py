import frappe


def get_context(context):
    # Fetch all shops where 'Available For Lease' is checked (true)
    context.shops = frappe.get_all(
        "Shop",
        fields=["name", "number", "area", "lease_fee_per_month", "tenant"],
        filters={"available_for_lease": 1},
    )
