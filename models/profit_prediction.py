def predict_profit(
    revenue
):

    profit_margin = 0.22

    profit = (
        revenue *
        profit_margin
    )

    return round(
        profit,
        2
    )