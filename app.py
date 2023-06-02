import sqlite3
from flask import Flask, make_response, request, render_template

app = Flask(__name__)


@app.route('/homepage')
def homepage():
    return render_template('homepage.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/men')
def men():
    return render_template('mens.html')


@app.route('/woman')
def women():
    return render_template('women.html')


@app.route('/shoes')
def shoes():
    return render_template('shoes.html')


@app.route('/clothing')
def clothing():
    return render_template('clothing.html')


@app.route('/bags')
def bags():
    return render_template('bags.html')


@app.route('/smart-watches')
def smart_watches():
    return render_template('smart-watches.html')


@app.route('/mens-jackets')
def mens_jackets():
    return render_template('mens-jackets.html')


@app.route('/sign-in', methods=["POST", "GET"])
def sign_in():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    if request.method == 'GET':
        return render_template('sign-in.html')
    else:
        email = request.form['email']
        password = request.form['password']
        if not email or not password:
            return render_template('sign-in.html', message='Email or password is empty')

        query = "SELECT COUNT(email) FROM users WHERE email = '{}'".format(email)
        cursor.execute(query)
        result = cursor.fetchone()

        if result[0] == 0:
            return render_template('sign-in.html', message='That account does not exist.')

        return render_template('sign-in.html', message='You are signed in.')


@app.route('/create-account', methods=["POST", "GET"])
def create_account():
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    if request.method == 'GET':
        return render_template('create-account.html')
    else:
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        password_confirmation = request.form['password_confirmation']

        if password != password_confirmation:
            return render_template('create-account.html', message='Passwords don\'t match.')

        if not email or not password or not username:
            return render_template('create-account.html', message='Email, password or username are empty')

        query = "INSERT INTO main.users (username, email, password) VALUES('{}', '{}', '{}')".format(username, email, password)

        cursor.execute(query)
        conn.commit()
        conn.close()

        return render_template('sign-in.html', message='Your account has been created. Please sign in.')


if __name__ == "__main__":
    app.run()
