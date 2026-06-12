from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session

from database.mysql_db import mysql

product_bp = Blueprint(
    'product',
    __name__
)

@product_bp.route('/products')
def products():

    if 'user_id' not in session:
        return redirect('/')

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT * FROM products"
    )

    products = cur.fetchall()

    cur.close()

    return render_template(
        'products.html',
        products=products
    )


@product_bp.route(
    '/add_product',
    methods=['GET','POST']
)
def add_product():

    if request.method == "POST":

        name = request.form['name']
        category = request.form['category']
        price = request.form['price']
        stock = request.form['stock']
        supplier = request.form['supplier']

        cur = mysql.connection.cursor()

        cur.execute(
            """
            INSERT INTO products
            (product_name,category,price,
            stock,supplier)

            VALUES(%s,%s,%s,%s,%s)
            """,
            (name,category,
             price,stock,supplier)
        )

        mysql.connection.commit()

        cur.close()

        return redirect('/products')

    return render_template(
        'add_product.html'
    )


@product_bp.route(
    '/delete_product/<int:id>'
)
def delete_product(id):

    cur = mysql.connection.cursor()

    cur.execute(
        "DELETE FROM products WHERE id=%s",
        (id,)
    )

    mysql.connection.commit()

    cur.close()

    return redirect('/products')