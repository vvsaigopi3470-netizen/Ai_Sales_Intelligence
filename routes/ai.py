from flask import Blueprint, render_template, request

from models.sales_forecast import predict_sales
from models.inventory_optimizer import optimize_inventory
from models.profit_prediction import predict_profit
from models.customer_segmentation import segment_customers

ai_bp = Blueprint('ai', __name__)


@ai_bp.route('/forecast', methods=['GET', 'POST'])
def forecast():

    prediction = None

    if request.method == 'POST':
        month = int(request.form['month'])
        prediction = predict_sales(month)

    return render_template(
        'forecast.html',
        prediction=prediction
    )


@ai_bp.route('/inventory_ai', methods=['GET', 'POST'])
def inventory_ai():

    result = None

    if request.method == 'POST':
        predicted_sales = int(request.form['sales'])
        result = optimize_inventory(predicted_sales)

    return render_template(
        'inventory_ai.html',
        result=result
    )


@ai_bp.route('/segmentation')
def segmentation():

    customers = segment_customers()

    return render_template(
        'segmentation.html',
        customers=customers
    )


@ai_bp.route('/profit_prediction', methods=['GET', 'POST'])
def profit_prediction():

    profit = None

    if request.method == 'POST':
        revenue = float(request.form['revenue'])
        profit = predict_profit(revenue)

    return render_template(
        'profit_prediction.html',
        profit=profit
    )
