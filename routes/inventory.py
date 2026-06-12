from flask import Blueprint, render_template, request, redirect, session
from database.mysql_db import mysql

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/inventory')
def inventory():
    if 'user_id' not in session:
        return redirect('/')

    cur = mysql.connection.cursor()
    cur.execute(
        """
        SELECT
            inventory.id,
            products.product_name,
            inventory.stock_level,
            inventory.reorder_point
        FROM inventory
        JOIN products
            ON inventory.product_id = products.id
        """
    )
    inventory_data = cur.fetchall()
    cur.close()

    return render_template(
        'inventory.html',
        inventory=inventory_data
    )
@inventory_bp.route(
    '/add_inventory',
    methods=['GET', 'POST']
)
def add_inventory():

    cur = mysql.connection.cursor()

    cur.execute(
        "SELECT id, product_name FROM products"
    )

    products = cur.fetchall()

    if request.method == "POST":

        product_id = request.form['product_id']
        stock_level = request.form['stock_level']
        reorder_point = request.form['reorder_point']

        cur.execute(
            """
            INSERT INTO inventory
            (
                product_id,
                stock_level,
                reorder_point
            )
            VALUES (%s,%s,%s)
            """,
            (
                product_id,
                stock_level,
                reorder_point
            )
        )

        mysql.connection.commit()

        return redirect('/inventory')

    return render_template(
        'add_inventory.html',
        products=products
    )

@inventory_bp.route('/delete_inventory/<int:id>')
def delete_inventory(id):
    cur = mysql.connection.cursor()
    cur.execute(
        """
        DELETE FROM inventory
        WHERE id = %s
        """,
        (id,)
    )
    mysql.connection.commit()
    cur.close()

    return redirect('/inventory')

@inventory_bp.route('/low_stock')
def low_stock():

    cur = mysql.connection.cursor()

    cur.execute(
        """
        SELECT *
        FROM inventory
        WHERE stock_level
        <= reorder_point
        """
    )

    low_stock_items = cur.fetchall()

    cur.close()

    return render_template(
        'low_stock.html',
        items=low_stock_items
    )