from flask import Flask,jsonify
import psycopg2
from flask_login import LoginManager
app = Flask(__name__)
app.config['SECRET_KEY'] = 'the random string'
from psycopg2 import sql
#conn = psycopg2.connect(dbname='BD', user='postgres', password='go3492717', host='127.0.0.1')
conn = psycopg2.connect(dbname='d40c9kou878e1a', user='ajxmqsujnfpwgq', password='e7bda57c460dda3a92231cf0eeefb70427d5fcc822da29b18750118d3ac350a2', host='ec2-54-247-177-254.eu-west-1.compute.amazonaws.com')
from app import database
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'#
login_manager.login_view = 'login'
from app import routes
if __name__ == '__main__':
    app.run(debug=True)
