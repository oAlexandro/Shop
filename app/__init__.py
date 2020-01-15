from flask import Flask,jsonify
import psycopg2
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
from psycopg2 import sql
conn = psycopg2.connect(dbname='BD', user='postgres', password='go3492717', host='127.0.0.1')
from app import database
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'#
login_manager.login_view = 'login'
from app import routes

