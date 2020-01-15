from _md5 import md5

from flask_login import UserMixin
from werkzeug.security import generate_password_hash,  check_password_hash
from app import login_manager
from app import conn


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)

class User(UserMixin):
    def __init__(self, id):
        self.id = id

    def set_status(self, status):
        self.status = status
        self.set_name()
        self.set_username()
        self.set_email()


    def set_name(self):
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM {} WHERE id = '{}'".format(self.status,self.id))
        name = cursor.fetchone()
        self.name = name[0]

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=retro&s={}'.format(digest, size)

    def set_username(self):
        cursor = conn.cursor()
        cursor.execute("SELECT login FROM {} WHERE id = '{}'".format(self.status, self.id))
        username = cursor.fetchone()
        self.username = username[0]

    def set_email(self):
        cursor = conn.cursor()
        cursor.execute("SELECT email FROM {} WHERE id = '{}'".format(self.status, self.id))
        email = cursor.fetchone()
        self.email = email[0]

