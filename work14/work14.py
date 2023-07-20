import sqlite3

#под к базе данных
connection = sqlite3.connect('my_users.db')

#perevodchik s python na sql
sql = connection.cursor()

#sozdanie tablici users
sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT);')

#dobavlenie novix dannix
sql.execute('INSERT INTO users (user_id, username) VALUES (0, "@pav_ok");')

#получить данные из таблицы
sql.execute('SELECT username FROM users;')

#Чтобы сделать некий отфильтрованный запрос который смог бы вывести нам к примеру данные определенного человека
print(sql.execute('SELECT username FROM users WHERE user_id=0;').fetchall())

#Чтобы обновить данные существующего к примеру пользователя используется ключевое слово UPDATE
sql.execute('UPDATE users SET username="@pasha_23" WHERE user_id=0;')
print(sql.execute('SELECT username FROM users;').fetchall())

#Чтобы удалить некие данные из таблицы баз данных используется ключевое слово DELETE
sql.execute('DELETE from users WHERE user_id=0;')

#fiksiruem izmenenie
connection.commit()