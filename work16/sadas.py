import telebot, buttons, db

from geopy import Nominatim

#Подключение к боту
bot = telebot.TeleBot('6214922741:AAH3JDGlOwrjjqWudrPIGxLMmR3kNFeuAt0')
#Работа с локацией
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                  'AppleWebKit/537.36 (KHTML, like Gecko)'
                                  'Chrome/114.0.0.0'
                                  'Safari/537.36')
#Временные данные
users = {}


#Прописываем обработку команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    check_user = db.checker(user_id)
    #Проверка на наличие пользователя в базе данных
    if check_user:
        products = db.get_pr_name_id()
        print(products)
        bot.send_message(user_id, 'Добро пожаловать!',
                         reply_markup=buttons.main_menu_buttons(products))
    else:
        bot.send_message(user_id, 'Здравствуйте запишите ваше имя!')
        #Перевести на этап получения имени
        bot.register_next_step_handler(message, get_name)

#Этап получения имени
def get_name(message):
    user_name = message.text
    bot.send_message(user_id, 'Отлично, а теперь отпарвьте свой номер!',
                     reply_markup=buttons.num_button())
    #Перевести на этап получения номера
    bot.register_next_step_handler(message, get_number, user_name)

#Этап получения номера
def get_number(message, user_name):
    #Если пользователь отправил контакт через кнопку
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'А теперь отправьте свою локацию!',
                         reply_markup=buttons.loc_button())
        #Перевести на этап получения локации
        bot.register_next_step_handler(message, get_location, user_name, user_number)
    #Если не через кнопку
    else:
        bot.send_message(user_id, 'Отправьте сообщение через кнопку!')
        bot.register_next_step_handler(message, get_number, user_name)

@bot.callback_query_handler(lambda call: call.data == 'cart')
def cart_handle(call):
    user = call.message.chat.id
    message_id = call.message.message_id

    bot.edit_message_text('Корзина',
                          user, message_id, reply_markup=buttons.cart_buttons())

def get_location(message, user_name, user_number):
    #Если пользователь отправил локацию через кнопку
    if message.location:
        user_location = geolocator.reverse(f"{message.location.longitude},"
                                           f"{message.location.latitude}")
        #Регистрируем пользователя
        db.register(user_id, user_name, user_number, user_location)
        bot.send_message(user_id, 'Вы успешно зарегистрировались!')
    #Если не через кнопку
    else:
        bot.send_message(user_id, 'Отправьте сообщение через кнопку!')
        bot.register_next_step_handler(message, get_location, user_name, user_number)

#Функция выбора товара
@bot.callback_query_handler(lambda call: int(call.data) in db.get_pr_id())
def get_user_product(call):
    chat_id = call.message.chat_id

    users[chat_id] = {'pr_name': call.data, 'pr_count': 1}

    message_id = call.message.message_id

    bot.edit_message_text('Выберите количество',
                          chat_id=chat_id, message_id=message_id,
                          reply_markup=buttons.choose_product_count())

#Запуск бота
bot.polling(non_stop=True)







from telebot import types

#Кнопка для отправки номера
def num_button():
    #Создаем пространство для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #Создаем сами кнопки
    num = types.KeyboardButton('Поделиться контактом', request_contact=True)

    #Добавляем кнопки в пространство
    kb.add(num)
    return kb

#Кнопка для отправки локации
def loc_button():
    # Создаем пространство для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    # Создаем сами кнопки
    loc = types.KeyboardButton('Поделиться геопозицией', request_location=True)

    # Добавляем кнопки в пространство
    kb.add(loc)
    return kb

def remove():
    types.ReplyKeyboardRemove()

#Кнопки для вывода товаров
def main_menu_buttons(products_from_db):
    #Создаем пространство для кнопок
    kb = types.InlineKeyboardMarkup(row_width=2)

    #Создаем несгораемую кнопку корзины
    cart = types.InlineKeyboardButton(text='Корзина', callback_data='cart')
    #Создаем кнопки c продуктами
    all_products = [types.InlineKeyboardButton(text=f'{i[1]}',
                    callback_data=i[1])
                    for i in products_from_db]

    #Объединяем кнопки с пространством
    kb.row(cart)
    kb.add(*all_products)

    #Возвращаем пространство
    return kb

#Кнопки выбора количества
def choose_product_count(current_amount=1, plus_or_minus=''):
    #Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=3)

    #Создаем несгораемые кнопки
    back = types.InlineKeyboardButton(text='Назад', callback_data='back')
    plus = types.InlineKeyboardButton(text='+', callback_data='increment')
    minus = types.InlineKeyboardButton(text='-', callback_data='decrement')
    count = types.InlineKeyboardButton(text=str(current_amount), callback_data=str(current_amount))
    add_to_cart = types.InlineKeyboardButton(text='Добавить в корзину', callback_data='to_cart')

    #Отслеживание плюса и минуса
    if plus_or_minus == 'increment':
        new_amount = int(current_amount) + 1

        count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))
    elif plus_or_minus == 'increment':
        if int(current_amount) > 1:
            new_amount = int(current_amount) - 1

            count = types.InlineKeyboardButton(text=str(new_amount), callback_data=str(new_amount))

    #Объединяем кнопки с пространством
    kb.add(minus, count, plus)
    kb.row(add_to_cart)
    kb.row(back)

    return kb

#Кнопки корзины
def cart_buttons():
    #Создаем пространство
    kb = types.InlineKeyboardMarkup(row_width=1)

    #Создаем кнопки
    clear_cart = types.InlineKeyboardButton(text='Очистить корзину',
                                            callback_data='clear_cart')
    order = types.InlineKeyboardButton(text='Оформить заказ',
                                       callback_data='order')
    back = types.InlineKeyboardButton(text='Назад',
                                      callback_data='back')
    #Объединяем кнопки с пространством
    kb.add(clear_cart, order, back)
    return kb
