from flask_login import UserMixin #класс с методами для аунтификации пользователей

class User(UserMixin): #класс User будет иметь все функциональные возможности, предоставляемые UserMixin
    def __init__(self, id, email, password, name):
        self.id = id #присваивает значение id атрибуту id экземпляра пользователя
        self.email = email #присваивает значение email атрибуту email
        self.password = password # присваивает значение password атрибуту password
        self.name = name # присваивает значение name атрибуту name

# Заглушка для хранения пользователей (словарь)
users_db = {} 
