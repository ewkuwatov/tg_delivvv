#data_base

import sqlite3

#Подключение к базе данных
connection = sqlite3.connect('tq_bot.db', check_same_thread=False)
#Связь между Python и SQL
sql = connection.cursor()

#Создание таблицы пользователей
sql.execute('CREATE TABLE IF NOT EXISTS users '
            '(id INTEGER,'
            'name TEXT,'
            'number TEXT,'
            'location TEXT);')

#Создание таблицы продуктов
sql.execute('CREATE TABLE IF NOT EXISTS products'
            '(pr_id INTEGER PRIMARY KEY AUTOINCREMENT,'
            'pr_name TEXT,'
            'pr_amount INTEGER,'
            'pr_price REAL,'
            'pr_des TEXT,'
            'pr_photo TEXT);')

#Создадим таблицу корзины пользователя
sql.execute('CREATE TABLE IF NOT EXISTS user_cart'
            '(user_id INTEGER,'
            'user_product TEXT,'
            'product_quantity INTEGER,'
            'total REAL);')

##Методы для пользователя##

#Регистрация
def register(id, name, number, location):
    sql.execute('INSERT INTO users VALUES (?, ?, ?, ?);',
                (id, name, number, location))
    #Фиксируем изменения
    connection.commit()

#Проверка на регистрацию
def checker(id):
    check = sql.execute('SELECT id FROM users WHERE id = ?;', (id,))

    if check.fetchone():
        return True
    else:
        return False



##Методы для продуктов##
#Вывод информации о конкретном продукте
def show_info(pr_name):
    sql.execute('SELECT pr_name, pr_des, '
                'pr_amount, pr_price, pr_photo'
                'WHERE pr_name = ?;', (pr_name,)).fetchone()


#Добавление товаров
def add_product(pr_name, pr_amount, pr_prize, pr_des, pr_photo):
    sql.execute('UNSERT INTO products (pr_name,'
                ' pr_amount, '
                'pr_prize, '
                'pr_des, '
                'pr_photo) VALUES (?, ?, ?, ?, ?);',
                (pr_name, pr_amount, pr_prize, pr_des, pr_photo))

    #Фиксируем изменения
    connection.commit()

#Вывод всех продуктов из базы
def get_all_products():
    add_products = sql.execute('SELECT * FROM products;')

    return  add_products.fetchall()

#Вывод id товаров
def get_pr_name_id():
    products = sql.execute('SELECT pr_id, pr_name, '
                           'pr_amount FROM products;').fetchall()

    return products


def get_pr_id():
    prods = sql.execute('SELECT pr_name, pr_id, pr_amount FROM products;').fetchall()
    sorted_prods = [i[1] for i in prods if i[2] > 0]
    return sorted_prods

##Методы для корзины##
def add_to_cart(user_id, user_pr, pr_quantity, user_total=0):
    sql.execute('INSERT INTO user_card VALUES (?, ?, ?, ?)',
                user_id, user_pr, pr_quantity, user_total)
    #Фиксируем ищменение
    connection.commit()

#Удаление
def del_from_cart(user_id):
    sql.execute('DELETE FROM user_card WHERE user_id=?;', (user_id))

    connection.commit()

#Отображение
def show_cart(user_id):
    cart = sql.execute('SELECT user_product,'
                'product_quantity,'
                'total FROM user_card WHERE user_id=?;', (user_id,)).fetchone()
    return cart

