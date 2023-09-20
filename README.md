## Список зависимостей
* blinker==1.6.2
* click==8.1.7 
* colorama==0.4.6
* Flask==2.3.3
* importlib-metadata==6.8.0
* itsdangerous==2.1.2
* Jinja2==3.1.2
* MarkupSafe==2.1.3
* psycopg==3.1.10
* psycopg2==2.9.7
* pyreqs==0.1.1
* sh==2.0.6
* typing_extensions==4.8.0
* tzdata==2023.3
* Werkzeug==2.3.7
* zipp==3.17.0

Все они указаны в файле requirements.txt для удобной установки
## Инструкция по установке и запуску
Для разработки веб-приложения был использован
flask фреймворк.

* Установка всех библиотек<br>
Чтобы установить все нужные библиотеки, достаточно прописать в terminal команду<br>
pip install -r .\requirements.txt
* Установка **Postgresql**<br>
 Для работы с базой данных был выбран **Postgresql**. Устанавливаем его с официального сайта
* Загрузка базы данных<br>
 Чтобы создать базу данных надо запустить **pgAdmin 4** и там запустить скрипт "init-db.sql". После чего
появится база данных Test, в которой будет две таблицы: users и passwords
* Запуск приложения<br>
При запуске приложения может возникнуть ошибка (и не одна). Связано это с тем, что может
отличаться порт, а также пароль к базе данных. Для этого надо поменять в коде пару мест,
которые помечены комментариями **change**. Узнать порт можно в **pgAdmin**.

После запуска появиться ip, нажав на который откроется приложение.
На главной странице три гиперссылки: users, login search и id search.
* users : показывает id и login активных пользователей<br>
* login search : показывает id и login пользователя с логином "admin"<br>
 В запросе можно менять login и будет выводиться информация о другой пользователе
* id search : показывает id и login пользователя с id = 3<br>
 В запросе можно менять значение id и будет выводиться информация о другой пользователе
