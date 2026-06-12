from flask import Blueprint
from flask import render_template
from flask import request

from models.recommendation_engine import (
    get_recommendations
)

intelligence_bp = Blueprint(
    'intelligence',
    __name__
)

@intelligence_bp.route(
    '/recommendation',
    methods=['GET','POST']
)
def recommendation():

    products = None

    if request.method == "POST":

        product = request.form['product']

        products = get_recommendations(
            product
        )

    return render_template(
        "recommendations.html",
        products=products
    )

@intelligence_bp.route(
    '/assistant',
    methods=['GET','POST']
)
def assistant():
    answer = None

    if request.method == "POST":
        question = request.form[
            'question'
        ].lower()

        if "sales" in question:
            answer = """
            Sales performance is healthy.
            Revenue trend is increasing.
            """

        elif "inventory" in question:
            answer = """
            Inventory levels are stable.
            No critical stock shortage found.
            """

        elif "customer" in question:
            answer = """
            Customer engagement is growing.
            Loyal customers contribute significantly.
            """

        elif "revenue" in question:
            answer = """
            Revenue is showing positive growth.
            Forecast indicates increasing demand.
            """

        elif "forecast" in question:
            answer = """
            AI Forecast predicts continued
            sales growth in upcoming months.
            """

        else:
            answer = """
            Please ask about:
            Sales,
            Customers,
            Inventory,
            Revenue,
            Forecast
            """

    return render_template(
        'ai_assistant.html',
        answer=answer
    )

@intelligence_bp.route('/reports')
def reports():

    return render_template(
        'reports.html'
    )
