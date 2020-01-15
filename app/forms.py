# -*- coding: utf-8 -*-
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, SelectField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError,Length
from flask_login import current_user
from app import app, conn
from flask_login import LoginManager
cursor = conn.cursor()

class RegistrationForm(FlaskForm):
    Username = StringField('Username', validators=[DataRequired()])
    Email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    admin = BooleanField('admin')
    submit = SubmitField('Sign In')




class InsertProduct(FlaskForm):
    name_product=StringField('Username', validators=[DataRequired()])
    product_description=StringField('Name description', validators=[DataRequired()])
    image=StringField('Image', validators=[DataRequired()])
    price=IntegerField("Price",validators=[DataRequired()])
    quantity_in_stock=IntegerField("Quantity",validators=[DataRequired()])
    select=StringField('Name Select', validators=[DataRequired()])
    submit = SubmitField('Insert')

class Product(FlaskForm):
    id_product=IntegerField("id", validators=[DataRequired()])
    id_category = IntegerField("id_category", validators=[DataRequired()])
    name_product = StringField('Username', validators=[DataRequired()])
    product_description = StringField('Name description', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    list_id=list()
    list_id=IntegerField("id_list", validators=[DataRequired()])
  #  price = IntegerField("Price", validators=[DataRequired()])




class UpdateAccountForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update')

    def validate_username(username):
        print(username,"TEEEEST")
        if username.data != current_user.username:
            user =cursor.execute(' UPDATE login SET username from customer where id_customer = %s', (current_user.id,))#
            if user:
                raise ValidationError('That username is taken. Please choose a different one.')

   #def validate_email(self, email):
   #    if email.data != current_user.email:
   #        user = User.query.filter_by(email=email.data).first()
   #        if user:
   #            raise ValidationError('That email is taken. Please choose a different one.')