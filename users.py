#Предназначено для управления аутентификацией пользователей в веб-приложениях
from flask_login import UserMixin # UserMixin -класс методов, необходимых для работы с аунтификацией пользователей

class User(UserMixin): #Создание нового класса User, 
  #который наследует от UserMixin (User будет иметь все функции UserMixin)
    def __init__(self, id, email, password, name): # метод инициализации (конструктор) класса User, 
      #принимает четыре параметра
        self.id = id  #присваивает значение id атрибуту id экземпляра пользователя
        self.email = email #присваивает значение email атрибуту email
        self.password = password # присваивает значение password атрибуту password
        self.name = name # присваивает значение name атрибуту name

# Пример добавления пользователей в "базу данных"
users_db = {
    '1': User('1', 'user@example.com', 'password', 'Имя Пользователя'),
}
# создается словарь users_db (база данных с пользователями)
# ‘1’ – ключ, экземпляр класса User - значение

