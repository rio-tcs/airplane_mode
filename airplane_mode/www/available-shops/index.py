import frappe


def get_context(context):
    context.shops = frappe.get_all(
        "Shop",
        fields=[
            "shop_name",
            "number",
            "area",
            "lease_fee_per_month",
            "store_picture",
            "area_m2",
            "height_m",
            "condition",
        ],
        filters={"available_for_lease": 1},
    )
