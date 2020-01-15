
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Пожалуйста, войдите, чтобы открыть эту страницу."

cursor = conn.cursor()

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

class User(UserMixin):
	def __init__(self, id):
		self.id = id
	def __repr__(self):
		return "%d/%s/%s/%s/%d" % (self.id)

@login_manager.user_loader
def load_user(user_id):
	return User(user_id)

# не пускать если не авторизирован
@login_required

# проверка на авторизацию для логина
if current_user.is_authenticated:
	flash('Вы уже авторизированны')
	return redirect(url_for('account'))

# выход из профиля
@app.route('/logout')
@login_required
def logout():
	logout_user()
	flash('Вы вышли из профиля')
	return redirect(url_for('index'))

# получение из базы параметров авторизированного пользователя
cursor.execute('select name, login from account where id = %s',(current_user.id,))
user = cursor.fetchone()

# сравнение введенного пароля пользователем с существующим хешем
check_password_hash(password_Hash, password)
# если по данному password мог когда-то быть создан password_Hash то вернутся true иначе false
# создание хеша по паролю
generate_password_hash(password)
# вернет хеш созданный по данному паролю длинной 100 символов

# авторизация кусок обработки
cursor.execute('select id, passwordHash from account where login = %s', (form.username.data,))
user = cursor.fetchone()
if user is None or not check_password_hash(user[1], form.password.data):
	flash('Неверный логин или пароль')
	return redirect(url_for('login'))
id = user[0]
user_id = User(id)
login_user(user_id, remember = form.remember_me.data)
flash('Вы успешно авторизировались')
return redirect(url_for('index'))