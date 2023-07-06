import telebot, buttons

bot = telebot.TeleBot('5950048805:AAGpb5Q_6Wq_x_jgrFByX4jizuryrv0uvJA')

@bot.message_handler(commands=['start'])
def strat_message(message):
    print(message.from_user)
    bot.send_message(message.from_user.id, f'{message.from_user.first_name} привет!', reply_markup=buttons.choice_buttons())

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Рад знакомству!')
    elif message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, '😒')
    elif message.text.lower() == 'википедия':
        bot.send_message(message.from_user.id, 'введите слово', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, wiki)
    elif message.text.lower() == 'переводчик':
        bot.send_message(message.from_user.id, 'введите слово для перевода')
        bot.register_next_step_handler(message, translate)

def wiki(message):
    if message.text.lower() == 'че гевара':
        bot.send_message(message.from_user.id, 'Лучший в Аргентине, после Месси', )
        bot.register_next_step_handler(message, wiki)
    elif message.text.lower() == 'арнольд':
        bot.send_message(message.from_user.id, 'https://ru.wikipedia.org/wiki/%D0%A8%D0%B2%D0%B0%D1%80%D1%86%D0%B5%D0%BD%D0%B5%D0%B3%D0%B3%D0%B5%D1%80,_%D0%90%D1%80%D0%BD%D0%BE%D0%BB%D1%8C%D0%B4')
        bot.register_next_step_handler(message, wiki)
    else:
        bot.send_message(message.from_user.id, 'Увы, но я не знаю что это😭😭😭', reply_markup=buttons.choice_buttons())
        bot.register_next_step_handler(message, text_message)
def translate(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет --> Hello, Hi')
    elif message.text.lower() == 'пока':
        bot.send_message(message.from_user.id, 'пока --> bye')
    else:
        bot.send_message(message.from_user.id, "didn't get you(", reply_markup=buttons.choice_buttons())
        bot.register_next_step_handler(message, text_message)

bot.polling()