import sqlite3

#под к базе данных
connection = sqlite3.connect('my_users.db')

#perevodchik s python na sql
sql = connection.cursor()

#sozdanie tablici users
sql.execute('CREATE TABLE IF NOT EXISTS users (user_id INTEGER, username TEXT);')

#dobavlenie novix dannix
sql.execute('INSERT INTO users (user_id, username) VALUES (0, "@pav_ok");')


sql.execute('SELECT username FROM users;')


print(sql.execute('SELECT username FROM users WHERE user_id=0;').fetchall())

sql.execute('UPDATE users SET username="@pasha_23" WHERE user_id=0;')
print(sql.execute('SELECT username FROM users;').fetchall())

sql.execute('DELETE from users WHERE user_id=0;')

#fiksiruem izmenenie
connection.commit()