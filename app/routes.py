import logging
import json
import requests
import sys
from flask import abort
import cgi
from datetime import datetime

from flask_login import login_user, login_required, current_user, logout_user
from flask import Flask,request,render_template,jsonify
from werkzeug.urls import url_parse
from flask import Flask,request,render_template,jsonify
filename="person.json"
file=open(filename,mode='w')
from app import app
from flask import  redirect, url_for,flash
from werkzeug.security import generate_password_hash,check_password_hash
from app.forms import RegistrationForm,LoginForm,InsertProduct,Product,UpdateAccountForm
from app import conn

from flask_login import UserMixin,LoginManager
#from app import login_manager
cursor = conn.cursor()


login_manager = LoginManager()

login_manager.init_app(app)

login_manager.login_view = "login"

login_manager.login_message = "Пожалуйста, войдите, чтобы открыть эту страницу."

class User(UserMixin):

	def __init__(self, id_):

		self.id = id_




	def __repr__(self):

		return "%d/%d" % self.id





@login_manager.user_loader

def load_user(user_id):

	return User(user_id)


@app.route("/")
@app.route('/home2', methods=['GET','POST'])
def base():
     id=Product()
     id=id.id_product
     print(id)
     empList = []
     #test = {}
     empDict2 = {
         'id_product': [],
         'id_category': [],
         'name_of_product': [],
         'product_description': [],
         'image': [],
         'price': []
     }
     Takebd(empList,empDict2)
     print(empDict2)

     return render_template('/home2.html',empList=empList,empDict2=empDict2)

@app.route("/about")
def about():
    return render_template('about.html', title='About')





@app.route("/cart", methods=['GET','POST'])
def cart():
    cart_dict={}
    if request.method == 'GET':
        print("GET")
    if request.method == 'POST':
        firstName = request.form
        output = firstName
        cart_dict=output
        test_cart_dic=cart_dict.to_dict()
        empList=[]
        print(test_cart_dic)
        for emp in test_cart_dic:
            count =test_cart_dic[emp]
            empDict = {
                'id': emp[5],
                'count':count
            }
            empList.append(empDict)
        print(current_user.id,"ID")
        now = datetime.now()
        index=0
        time=False;
        if (current_user.is_authenticated):
            for cou in empList:
                print(empList[index]['id'])
                print(empList[index]['count'])
                cursor.execute(
                    "INSERT INTO ord (id_customer, id_order, id_product, name_of_product, product_description, image, price, date_order) "
                   "VALUES ((SELECT(id_customer) From customer WHERE %(id_user)s=id_customer),"
                   " (SELECT MAX(id_order)+1 From ord), (SELECT (id_product) From product WHERE (%(id_new_order)s)+1=id_product), (SELECT(name_of_product) From product WHERE (%(id_new_order)s)+1=id_product),(SELECT(product_description) From product WHERE (%(id_new_order)s)+1=id_product),(SELECT(image) From product WHERE (%(id_new_order)s)+1=id_product),"
                    "(Select price*%(count)s From product Where price=(Select price FROM product where (%(id_new_order)s)+1=id_product)), %(date_now)s)",
                   {'id_new_order': empList[index]['id'],
                    'count': empList[index]['count'],
                    'id_user': current_user.id,
                    'date_now':now.strftime("%Y-%m-%d")},

                    )
                conn.commit()

                print(empList[index]['id'])
                index=index+1
                print("Commit accept")
            time=True;
            print('COMIT ACEPT')
            return jsonify({'output': 'Full Name: ' })
        if(time==True):
            return render_template('cart.html', title='Cart')



@app.route("/order", methods=['GET','POST'])
def order():
    cursor.execute('Select id_customer, id_order, name_of_product, product_description, image, price, date_order from ord where id_customer=%(id)s',
                   {'id': current_user.id,
                   'name_of_product': 'name',
                    'select': {'select'},
                    'product_description': {'product'},
                    'image': {'image'},
                    'price': {'price'},
                    'quantity_in_stock': {'quantity'}
                    })
    order_t =cursor.fetchall()
    order_take=[]
    for emp in order_t:
        dict = {
            'id_customer': emp[0],
            'id_order': emp[1],
            'name_of_product': emp[2],
            'product_description': emp[3],
            'image': emp[4],
            'price': emp[5],
            'date_order':emp[6]
        }
        order_take.append(dict)
    print(order_take)

    return render_template('order.html', title='Order',order_take=order_take)







def Takebd(empList,empDict2):
    cursor.execute('Select id_product,id_category,name_of_product,product_description,image,price from product ',
                   {'name_of_product': 'name',
                    'select': {'select'},
                    'product_description': {'product'},
                    'image': {'image'},
                    'price': {'price'},
                    'quantity_in_stock': {'quantity'}
                    })
    product_form = cursor.fetchall()
    id_colum = 0
    for emp in product_form:
       empDict = {
          'id_product': emp[0],
           'id_category': emp[1],
           'name_of_product': emp[2],
           'product_description': emp[3],
           'image': emp[4],
           'price': emp[5]
            }
       id_colum = id_colum + 1
       empList.append(empDict)
    for emp in product_form:
        empDict2['id_product'].append(emp[0])
        empDict2['id_category'].append(emp[1])
        empDict2['name_of_product'].append(emp[2])
        empDict2['product_description'].append(emp[3])
        empDict2['image'].append(emp[4])
        empDict2['price'].append(emp[5])
    return empList, empDict2

@app.route('/admin', methods=['GET','POST'])
@login_required
def adminPage():
    if (current_user.is_authenticated):
        id_user = current_user.id
        cursor = conn.cursor()
        cursor.execute('Select type_admin from customer where id_customer=%(id)s', {'id': id_user})
        login = cursor.fetchone()[0]
        form_insert = InsertProduct()
        if(login==True):
            if ('open') in request.form:
                print("It's working")
            if form_insert.validate_on_submit():
                name=form_insert.name_product.data
                product=form_insert.product_description.data
                image=form_insert.image.data
                price=form_insert.price.data
                quantity=form_insert.quantity_in_stock.data
                select=form_insert.select.data
                print(name,product,image,price,quantity,select)
                cursor.execute("INSERT INTO product (id_product,id_category, name_of_product, product_description,image,price,quantity_in_stock) "
                               "VALUES ((SELECT MAX(id_product)+1 From product),"
                               "(SELECT (id_category) From category WHERE %(select)s=name_category), %(name_of_product)s,  %(product_description)s, %(image)s, %(price)s, %(quantity_in_stock)s)",
                               {'name_of_product': name,
                                'select': select,
                                'product_description': product,
                                'image': image,
                                'price': price,
                                'quantity_in_stock': quantity})
                conn.commit()
        else:
            return redirect('/login')

    return render_template('admin.html', title='Register', form=form_insert)

@app.route('/')
def mainPage():
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('base'))
    form_register = RegistrationForm()
    if form_register.validate_on_submit():

            cursor = conn.cursor()
            form_register.password.data = generate_password_hash(form_register.password.data)
            if form_register.Username != login:
                print("Создавай")
            cursor.execute("INSERT INTO customer (id_customer,login, password, email) "
                           "VALUES ((SELECT MAX(id_customer)+1 From customer), %(username)s,  %(password)s, %(email)s)",
                           {'username' : form_register.Username.data,
                            'password': str(form_register.password.data),
                            'email' : form_register.Email.data})
            conn.commit()
            flash(f'Account created for {form_register.Username.data}!', 'success')
            return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form_register)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('base'))
    login_form = LoginForm()
    if login_form.validate_on_submit():
        cursor = conn.cursor()
        try:
            username = login_form.username.data
            password = login_form.password.data
            cursor.execute('SELECT * FROM customer where login=%(login)s', {'login': username})
            user = cursor.fetchone()
            if (user != None and check_password_hash(user[2],password)):
                print("coorect password")
                bool=True
                if (user[4] == bool):
                    id = user[0]
                    user_id = User(id)
                    login_user(user_id, remember=login_form.remember_me.data)#
                    return redirect('admin')
                id = user[0]
                user_id = User(id)
                login_user(user_id, remember=login_form.remember_me.data)
                return redirect('/home2')
            else:
                flash("Please check login and password", 'danger')
        except:
            flash("Enter u infa", 'danger')
    return render_template('login.html', form=login_form)

@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash("You have been logged out.")
    return redirect(url_for('login'))

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    cursor.execute('select login,email from customer where id_customer = %s', (current_user.id,))
    print("TEST current",current_user.id)
    user = cursor.fetchone()
    form = UpdateAccountForm()
    print("TEST VALIDATE")
    if request.method == 'POST':
        current_user.username = form.username.data
        current_user.email = form.email.data
        #form.submit(current_user.username)
        id_test=current_user.id
        print(current_user.username,current_user.email,current_user.id)
        cursor.execute('SELECT email FROM customer where id_customer=%(id)s', {'id': current_user.id})
        email = cursor.fetchone()[0]
        print(email)
        if(email==current_user.email):
            print("UPDATE",form.username.data,id_test)
            print("UPDATE", form.username.data, id_test)
            cursor.execute('UPDATE customer SET login=%(login)s where id_customer=%(id)s', {'id': id_test, 'login':form.username.data})
            conn.commit()
            flash('Your account has been updated!', 'success')
            return redirect(url_for('account'))
    return render_template('account.html', title='Account',user=user,form=form)


