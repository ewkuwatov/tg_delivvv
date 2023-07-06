#Main file
import telebot, buttons, db

from geopy import Nominatim

#Поддлючение к боту
bot = telebot.TeleBot('6312288665:AAHv4OLdrsbSF4pR4faiOKk10cZVjnPaIc4')

#Работа с локацией
geolocator = Nominatim(user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
                                  ' AppleWebKit/537.36 (KHTML, like Gecko)'
                                  ' Chrome/114.0.0.0 '
                                  'Safari/537.36')
users = {}


#Прописываем обработку команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.id
    check_user = db.checker(user_id)

    #Проверка на наличие пользователя в бозе данных
    if check_user:
        products = db.get_all_products()
        print(products)

        bot.send_message(user_id, 'Welcome!', reply_markup=buttons.main_menu_buttons(products))

    else:
        bot.send_message(user_id, 'Hello, type your name!')
        #Перевести на этап получение имени
        bot.register_next_step_handler(message, get_name)

def get_name(message):
    user_name = message.text
    bot.send_message(user_id, 'Great, now send your number!',
                     reply_markup=buttons.num_button())

    #Перевести на этап получение номера
    bot.register_next_step_handler(message, get_number, user_name)

#Этап получение номера
def get_number(message, user_name):
    #Если пользователь отправил контакт через кнопку
    if message.contact:
        user_number = message.contact.phone_number
        bot.send_message(user_id, 'Now send your location!', reply_markup=buttons.loc_button())
        #Перевести на этап получение локации
        bot.register_next_step_handler(message, get_location, user_name, user_number)

    #Если не через кнопку
    else:
        bot.send_message(user_id, 'Send message through button!')
        bot.register_next_step_handler(message, get_number, user_name)

@bot.callback_query_handler(lambda call: call.data in ['increment', 'decrement', 'to_cart', 'back'])
def get_user_count(call):
    chat_id = call.message.chat.id

    if call.data == 'increment':
        actual_amount = users[chat_id]['pr_amount']

        users[chat_id]['pr_amount'] += 1
        bot.edit_message_reply_markup(chat_id=chat_id,
                                      message_id=call.message.message_id,
                                      reply_markup=buttons.choose_product_amount(actual_amount, 'increment'))
    elif call.data == 'decrement':
            actual_amount = users[chat_id]['pr_amount']

            users[chat_id]['pr_amount'] -= 1
            bot.edit_message_reply_markup(chat_id=chat_id,
                                          message_id=call.message.message_id,
                                          reply_markup=buttons.choose_product_amount(actual_amount, 'decrement'))
    elif call.data == 'back':
        products = db.get_pr_name_id()
        bot.edit_message_text('Выберите пункт меню: ',
                              chat_id,
                              call.message.message_id,
                              reply_markup=buttons.main_menu_buttons(products))
    elif call.data == 'to_cart':
        product_count = users[chat_id]['pr_count']
        total = users[chat_id]['pr_count'] * users[chat_id]['pr_price']
        user_product = users[chat_id]['pr_name']
        db.add_to_cart(chat_id, user_product, product_count, total)
        bot.edit_message_text('Продукт успешно добавлен!',
                              chat_id,
                              call.message.message_id,
                              reply_markup=buttons.main_menu_buttons(products))

@bot.callback_query_handler(lambda call: call.data == 'cart')
def cart_handle(call):
    user = call.message.chat.id
    message_id = call.message.message_id

    if call.data == 'clear_cart':
        db.del_from_cart(user)
        bot.edit_message_text('Корзина очищено!',
                              user,
                              message_id,
                              reply_markup=buttons.main_menu_buttons(products))

    elif call.data == 'order':
        db.del_from_cart(user)
        bot.send_message((791555605, 'Новый заказ!'))
        bot.edit_message_text('заказ оформлен',
                              user,
                              call.message.message_id,
                              reply_markup=buttons.main_menu_buttons(products))

    elif call.data == 'back':
        products = db.get_pr_name_id()
        bot.edit_message_text('Выберите пункт меню: ',
                              user,
                              call.message.message_id,
                              reply_markup=buttons.main_menu_buttons(products))

    elif call.data == 'cart':
        bot.edit_message_text('Корзина',
                              user,
                              call.message.message_id,
                              reply_markup=buttons.main_menu_buttons())

def get_location(message, user_name, user_number):
    #Если пользователь отправил локацию через кнопку
    if message.location:
        user_location = geolocator.reverse(f"{message.location.longitude},"
                                           f"{message.location.latitude}")
        #Регистрируем пользователя
        db.register(user_id, user_name, user_number, user_location)
        bot.send_message(user_id, 'Вы успешно зарегистрировались!', reply_markup=buttons.remove())

    # Если не через кнопку
    else:
        bot.send_message(user_id, 'Отправьте сообщение через кнопку!')
        bot.register_next_step_handler(message, get_location, get_name, user_number)

#Функция выбора товара
@bot.callback_query_handler(lambda call: int(call.data) in db.get_pr_id())
def get_user_product(call):
    chat_id = call.message.chat.id

    users[chat_id] = {'pr_name': call.data, 'pr.count': 1}

    message_id = call.message.message_id

    bot.edit_message_text('Выберите количество',
                            chat_id=chat_id, message_id=message_id,
                            reply_markup=buttons.choose_product_count())
#Запуск бота
bot.polling(non_stop=True)
