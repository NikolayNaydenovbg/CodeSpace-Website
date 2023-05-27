import mysql.connector
from flask import Flask, make_response, request

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='930826',
    port='3306',
    database='michal_kors'
)

app = Flask(__name__)


@app.route('/about')
def public():
    cursor = mydb.cursor()

    cursor.execute('SELECT * FROM users')

    users = cursor.fetchall()

    return make_response(users)

@app.route('/users')
def index():
    cursor = mydb.cursor()

    cursor.execute('SELECT * FROM users')

    users = cursor.fetchall()

    return make_response(users)


@app.route('/users', methods=["POST"])
def index_post():
    cursor = mydb.cursor()

    cursor.execute('SELECT * FROM users')

    users = cursor.fetchall()
    print(request.get_json())
    return make_response("HEllo!")


if __name__ == "__main__":
    app.run()
