from flask import Flask, render_template, request
import psycopg2
import psycopg2.extras

app = Flask(__name__)
app.secret_key = "cairocoders-ednalan"


DB_HOST = "localhost"
DB_NAME = "Test"
DB_USER = "postgres"
DB_PASS = "123" #change password

conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=5433) #change port


@app.route('/users')
def users():
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "select id, login from users where status = 1"
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template("users.html", list_users=list_users)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/by-id')
def id_():
    _id = request.args.get('id')

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "select id, login from users where id = " + _id
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template("id.html", list_users=list_users)


@app.route('/by-login')
def login_():
    login = request.args.get('login')

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    s = "select id, login from users where login=" + "\'" + login + '\''
    cur.execute(s)
    list_users = cur.fetchall()
    return render_template("login.html", list_users=list_users)


if __name__ == "__main__":
    app.run(debug=True)