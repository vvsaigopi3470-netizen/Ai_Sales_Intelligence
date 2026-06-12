def optimize_inventory(
    predicted_sales
):

    safety_stock = (
        predicted_sales * 0.25
    )

    reorder_point = (
        predicted_sales +
        safety_stock
    )

    return {

        "sales":
        predicted_sales,

        "safety_stock":
        round(safety_stock),

        "reorder":
        round(reorder_point)
    }