import psycopg2
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for, Response
#from flask_login import LoginManager, UserMixin, logout_user, login_required, login_user, current_user
from psycopg2 import sql
#app = Flask(name)
app.config.update(
    DEBUG = True,
    SECRET_KEY = 'secret'
)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

try:
    conn = psycopg2.connect(dbname='BD', user='postgres',
                            password='go3492717', host='127.0.0.1')
except:
    print('Error connect')

cursor = conn.cursor()
def createDatabase():

    try:

        cur.execute(

            "CREATE TABLE if not exists person (user_id serial primary key, login varchar(15) NOT null unique, password TEXT NOT NULL, status TEXT NOT NULL, email TEXT NOT NULL unique, phone TEXT NOT NULL unique);")

        conn.commit()
    except Exception as e:

        print(e)

connection.commit()