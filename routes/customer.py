from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect

from database.mysql_db import mysql

customer_bp = Blueprint(
    'customer',
    __name__
)

@customer_bp.route('/customers')
def customers():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT * FROM customers"
    )

    customers = cur.fetchall()

    cur.close()
    return render_template(
        'customers.html',
        customers=customers
    )

@customer_bp.route(
    '/add_customer',
    methods=['GET','POST']
)
def add_customer():

    if request.method == "POST":

        name = request.form['name']
        city = request.form['city']
        phone = request.form['phone']

        cur = mysql.connection.cursor()

        cur.execute(
            """
            INSERT INTO customers
            (customer_name,
             city,
             phone)

            VALUES(%s,%s,%s)
            """,
            (name,city,phone)
        )

        mysql.connection.commit()

        cur.close()

        return redirect('/customers')

    return render_template(
        'add_customer.html'
    )