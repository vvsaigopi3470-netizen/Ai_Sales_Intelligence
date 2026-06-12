from flask import Blueprint
from flask import jsonify

from models.sales_forecast import (
    predict_sales
)

forecast_api = Blueprint(
    "forecast_api",
    __name__
)

@forecast_api.route(
    "/api/forecast/<int:month>"
)
def forecast(month):

    prediction = predict_sales(
        month
    )

    return jsonify({

        "month":month,

        "predicted_sales":
        prediction
    })