from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import send_file

from database.mysql_db import mysql


import pandas as pd

sales_bp = Blueprint(
    "sales",
    __name__
)
from utils.analytics import (
    generate_sales_chart
)

@sales_bp.route('/analytics')
def analytics():

    chart = generate_sales_chart()

    return render_template(
        'analytics.html',
        chart=chart
    )

@sales_bp.route('/sales')
def sales():

    cur = mysql.connection.cursor()

    cur.execute("""
        SELECT
        sales.id,
        products.product_name,
        customers.customer_name,
        sales.quantity,
        sales.revenue,
        sales.sale_date

        FROM sales

        JOIN products
        ON sales.product_id = products.id

        JOIN customers
        ON sales.customer_id = customers.id

        ORDER BY sales.id DESC
    """)

    data = cur.fetchall()

    cur.close()

    return render_template(
        "sales.html",
        sales=data
    )


@sales_bp.route(
    '/add_sale',
    methods=['GET','POST']
)
def add_sale():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT * FROM products"
    )

    products = cur.fetchall()

    cur.execute(
        "SELECT * FROM customers"
    )

    customers = cur.fetchall()

    if request.method == "POST":

        product_id = request.form['product']
        customer_id = request.form['customer']

        quantity = int(
            request.form['quantity']
        )

        cur.execute(
            """
            SELECT price
            FROM products
            WHERE id=%s
            """,
            (product_id,)
        )

        price = cur.fetchone()[0]

        revenue = quantity * price

        profit = revenue * 0.20

        cur.execute("""
            INSERT INTO sales(
                product_id,
                customer_id,
                quantity,
                revenue,
                unit_price,
                profit,
                sale_date
            )

            VALUES(
            %s,%s,%s,%s,%s,%s,CURDATE()
            )
        """,

        (
            product_id,
            customer_id,
            quantity,
            revenue,
            price,
            profit
        ))

        mysql.connection.commit()

        return redirect('/sales')

    return render_template(
        'add_sale.html',
        products=products,
        customers=customers
    )

@sales_bp.route(
    '/export_sales'
)
def export_sales():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT * FROM sales"
    )

    data = cur.fetchall()

    cur.close()

    df = pd.DataFrame(data)

    df.to_excel(
        'sales_report.xlsx',
        index=False
    )

    return send_file(
        'sales_report.xlsx',
        as_attachment=True
    )

@sales_bp.route(
    '/delete_sale/<int:id>'
)
def delete_sale(id):

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM sales WHERE id=%s",
        (id,)
    )

    mysql.connection.commit()

    cur.close()

    return redirect('/sales')