from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import session
from flask import flash

from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from database.mysql_db import mysql

auth_bp = Blueprint(
'auth',
__name__
)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']

        cur = mysql.connection.cursor()

        cur.execute(
            "SELECT * FROM users WHERE email=%s",
            (email,)
        )

        user = cur.fetchone()

        cur.close()

        if user:
            stored_password = user[3]

            try:
                valid = check_password_hash(
                    stored_password,
                    password
                )
            except:
                valid = (
                    stored_password == password
                )

            if valid:
                session['user_id'] = user[0]
                session['user_name'] = user[1]
                return redirect('/dashboard')

        flash(
            "Invalid Email or Password",
            "danger"
        )

    return render_template(
        'login.html'
)

@auth_bp.route(
'/register',
methods=['GET', 'POST']
)
def register():
    if request.method == "POST":
        fullname = request.form['fullname']
        email = request.form['email']
        password = request.form['password']

        hashed_password = generate_password_hash(
            password
        )

        cur = mysql.connection.cursor()

        cur.execute(
            """
            INSERT INTO users
            (fullname,email,password)
            VALUES(%s,%s,%s)
            """,
            (
                fullname,
                email,
                hashed_password
            )
        )

        mysql.connection.commit()

        cur.close()

        flash(
            "Registration Successful",
            "success"
        )

        return redirect('/')

    return render_template(
        'register.html'
    )

@auth_bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')

