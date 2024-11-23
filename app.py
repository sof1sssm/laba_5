#код представляет собой простое веб-приложение
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from users import User, users_db # Импортируем модель пользователя и базу данных

app = Flask(__name__) #Создает экземпляр приложения Flask, name - указывает на текущее имя модуля
login_manager = LoginManager(app) #создает экземпляр, который будет управлять аутентификацией пользователей
login_manager.login_view = 'login' #если пользователь не аутентифицирован, он будет перенаправлен на маршрут login

class User(UserMixin): #класс User, наследует от UserMixin, предоставляя методы для аутентификации
    def __init__(self, id, email, password, name): #Конструктор класса, инициализирует атрибуты пользователя
        self.id = id #присваивает значение id атрибуту id экземпляра пользователя
        self.email = email #присваивает значение email атрибуту email
        self.password = password # присваивает значение password атрибуту password
        self.name = name # присваивает значение name атрибуту name

@login_manager.user_loader #Декоратор, регистрирует функцию для загрузки пользователя по его идентификатору
def load_user(user_id): #Функция, которая возвращает пользователя из users_db по его идентификатору
    return users_db.get(user_id)

@app.route('/')
@login_required #Декоратор, требует, чтобы пользователь был аутентифицирован для доступа к маршруту '/'
def index(): #Функция, рендерит шаблон index.html, передавая имя текущего пользователя
    return render_template('index.html', name=current_user.name)

@app.route('/login', methods=['GET', 'POST']) #принимает как GET, так и POST запросы
# GET-запросы не могут менять данные на сервере, а лишь извлекают оттуда информацию
# POST-запросы, можно передавать данные на сервер для их обработки
def login():
    if request.method == 'POST': #Проверяет, был ли отправлен POST-запрос (т.е. пользователь пытается войти)
        email = request.form['email'] #Извлекает введенные пользователем данные
        password = request.form['password']
        
        user = next((u for u in users_db.values() if u.email == email), None) #Ищет пользователя по введенному email
        if user is None:
            flash('Пользователь не найден', 'error')
            return render_template('login.html')
        
        if user.password != password: #Проверяет, совпадает ли введенный пароль с сохраненным
            flash('Неверный пароль', 'error')
            return render_template('login.html')
        
        login_user(user) #Если аутентификация успешна, выполняет вход пользователя
        return redirect(url_for('index')) #Перенаправляет пользователя на гл. страницу после успешного входа
    
    return render_template('login.html') #Если это GET-запрос или произошла ошибка, рендерит страницу входа

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST': #Проверяет, был ли отправлен POST-запрос
        name = request.form['name'] # Извлекает данные из формы регистрации
        email = request.form['email']
        password = request.form['password']
        
        if any(u.email == email for u in users_db.values()): #Проверяет, существует ли уже пользователь с таким email
            flash('Пользователь с таким email уже существует', 'error')
            return render_template('signup.html')
        
        new_user_id = str(len(users_db) + 1) #Генерирует новый идентификатор для пользователя
        new_user = User(new_user_id, email, password, name) #Создает нового пользователя
        users_db[new_user_id] = new_user #Сохраняет нового пользователя в базе данных
        return redirect(url_for('login')) #Перенаправляет пользователя на страницу входа после успешной регистрации
    
    return render_template('signup.html') #Если это GET-запрос, рендерит страницу регистрации

@app.route('/logout')
@login_required #Требует, чтобы пользователь был аутентифицирован для выхода
def logout(): #Выходит из системы
    logout_user() #Выходит из системы
    return redirect(url_for('login')) #Перенаправляет пользователя на страницу входа после выхода

if __name__ == '__main__':
    app.run(debug=True)
