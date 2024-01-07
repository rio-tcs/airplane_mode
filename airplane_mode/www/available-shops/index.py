import frappe


def get_context(context):
    context.shops = frappe.get_all(
        "Shop",
        fields=[
            "shop_name",
            "number",
            "area",
            "lease_fee_per_month",
            "store_picture",  # Assuming 'image' is the field name for the shop image
            "area_m2",  # Assuming there is a 'length' field
            "height_m",  # Assuming there is a 'height' field
            "condition",  # Assuming there is a 'condition' field
        ],
        filters={"available_for_lease": 1},
    )
