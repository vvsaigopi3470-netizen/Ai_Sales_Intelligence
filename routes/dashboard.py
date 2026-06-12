from flask import Blueprint
from flask import render_template

from database.mysql_db import mysql

dashboard_bp = Blueprint(
    'dashboard',
    __name__
)

@dashboard_bp.route('/dashboard')
def dashboard():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM products"
    )
    products = cur.fetchone()[0]

    cur.execute(
        "SELECT COUNT(*) FROM customers"
    )
    customers = cur.fetchone()[0]

    cur.execute(
        "SELECT COUNT(*) FROM sales"
    )
    sales = cur.fetchone()[0]

    cur.execute(
        """
        SELECT IFNULL(
        SUM(revenue),0)
        FROM sales
        """
    )

    revenue = cur.fetchone()[0]

    cur.close()

    return render_template(
        'dashboard.html',
        products=products,
        customers=customers,
        sales=sales,
        revenue=revenue
    )


