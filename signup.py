#код представляет собой HTML-шаблон для страницы регистрации пользователя в веб-приложении
<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8"> #Устанавливает кодировку документа на UTF-8, что позволяет корректно отображать символы различных языков
    <meta name="viewport" content="width=device-width, initial-scale=1.0"> #устанавливая ширину в соответствии с шириной экрана устройства
    <title>Регистрация</title> #Устанавливает заголовок страницы
    <style> #CSS-стили, которые применяются к элементам на странице
        body { #Определяет стили для всего тела страницы
            background-color: #f0f8ff; /* Светлый фон */
            font-family: 'Arial', sans-serif; /* Шрифт */
            color: #333; /* Цвет текста */
            margin: 0;
            padding: 20px;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh; /* Высота экрана */
        }
        .container { # Стили для контейнера формы
            background-color: white; /* Цвет фона формы */
            border-radius: 8px; /* Закругленные углы */
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1); /* Тень */
            padding: 30px; /* Отступы внутри контейнера */
            width: 300px; /* Ширина формы */
        }
        h1 { #Стили для заголовка
            text-align: center; /* Центрирование заголовка */
            margin-bottom: 20px; /* Отступ снизу */
            color: #2c3e50; /* Цвет заголовка */
        }
        input[type="text"], #Стили для полей ввода
        input[type="email"],
        input[type="password"] {
            width: 100%; /* Ширина полей ввода */
            padding: 10px; /* Отступы внутри полей */
            margin: 10px 0; /* Отступы сверху и снизу */
            border: 1px solid #ccc; /* Цвет рамки */
            border-radius: 4px; /* Закругленные углы */
        }
        button { #Стили для кнопки
            width: 100%; /* Ширина кнопки */
            padding: 10px; /* Отступы внутри кнопки */
            background-color: #007bff; /* Цвет фона кнопки */
            color: white; /* Цвет текста кнопки */
            border: none; /* Убираем рамку */
            border-radius: 4px; /* Закругленные углы */
            cursor: pointer; /* Указатель при наведении */
        }
        button:hover {
            background-color: #0056b3; /* Цвет кнопки при наведении */
        }
        p {
            text-align: center; /* Центрирование текста */
        }
        a {
            color: #007bff; /* Цвет ссылки */
            text-decoration: none; /* Убираем подчеркивание */
        }
        a:hover {
            text-decoration: underline; /* Подчеркивание ссылки при наведении */
        }
    </style>
</head>
<body>
    <div class="container"> #Создает контейнер для формы регистрации с классом container
        <h1>Форма регистрации</h1> 
        {% with messages = get_flashed_messages(with_categories=true) %} #Использует шаблонный синтаксис Jinja2 для временных сообщений (ошибка, увед)
          {% if messages %} # Проверяет, есть ли сообщения для отображения
            <ul> #Открывает ненумерованный список для отображения сообщений
            {% for category, message in messages %} #Перебирает каждое сообщение и его категорию (например, "error" или "success")
              <li class="{{ category }}">{{ message }}</li> #Создает элемент списка для каждого сообщения, применяя соответствующий класс для стилизации.
            {% endfor %}
            </ul>
          {% endif %}
        {% endwith %}
        <form method="POST"> #Открывает форму, которая будет отправлять данные методом POST на сервер
            <input type="text" name="name" required placeholder="Имя">   
            <input type="email" name="email" required placeholder="Email">
            <input type="password" name="password" required placeholder="Пароль">
            <button type="submit">Зарегистрироваться</button>
        </form>
        <p><a href="{{ url_for('login') }}">Уже есть аккаунт? Войти</a></p>
    </div>
</body>
</html>

