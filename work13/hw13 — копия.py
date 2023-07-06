import telebot, currency_button, currency_button2

bot = telebot.TeleBot('6069119582:AAFP4MXHK-vWbfSyp9UJ-nX3fhEcDybR4io')

@bot.message_handler(commands=['start'])
def star_message(message):
    bot.send_message(message.from_user.id, f'{message.from_user.first_name} привет! Пожалуйста выберите услугу.', reply_markup=currency_button.choice_buttons())

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'валюта':
        bot.send_message(message.from_user.id, '💶 euro - 15000 uzs\n' + \
                                                '💵 dollar - 13500 uzs\n' + \
                                                '💷 pound - 14492 uzs',
        reply_markup=currency_button.choice_buttons())
        bot.register_next_step_handler(message, text_message)

    elif message.text.lower() == 'обмен валют':
        bot.send_message(message.from_user.id, 'Выберите валюту:\n' + \
                                               '💶 euro - 15000 uzs\n' + \
                                                '💵 dollar - 13500 uzs\n' + \
                                                '💷 pound - 14492 uzs', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, exchange)


def exchange(message):
    if message.text.lower() == 'euro':
        bot.send_message(message.from_user.id, 'Сколько количество денег хотите обменять: ', reply_markup=currency_button2.cur_buttons())
        bot.register_next_step_handler(message, euro)
    elif message.text.lower() == 'dollar':
        bot.send_message(message.from_user.id, 'Сколько количество денег хотите обменять: ', reply_markup=currency_button2.cur_buttons2())
        bot.register_next_step_handler(message, dollar)
    elif message.text.lower() == 'pound':
        bot.send_message(message.from_user.id, 'Сколько количество денег хотите обменять: ', reply_markup=currency_button2.cur_buttons3())
        bot.register_next_step_handler(message, pound)

def euro(message):
    if message.text == '💶 100 euro':
        x = 100*15000
        bot.send_message(message.from_user.id, f' 100 euro будет равняться {x} uzs')
        bot.register_next_step_handler(message, euro)
    elif message.text == '💶 200 euro':
        x = 200*15000
        bot.send_message(message.from_user.id, f' 200 euro будет равняться {x} uzs')
        bot.register_next_step_handler(message, euro)
    elif message.text == '💶 500 euro':
        x = 500*15000
        bot.send_message(message.from_user.id, f' 500 euro будет равняться {x} uzs')
        bot.register_next_step_handler(message, euro)
    elif message.text == '💶 1000 euro':
        x = 1000*15000
        bot.send_message(message.from_user.id, f' 1000 euro будет равняться {x} uzs')
        bot.register_next_step_handler(message, euro)
    elif message.text == '💶 2000 euro':
        x = 2000*15000
        bot.send_message(message.from_user.id, f' 2000 euro будет равняться {x} uzs')
        bot.register_next_step_handler(message, euro)
    elif message.text == 'Back':
        bot.send_message(message.from_user.id, 'Выберите валюту: \n' + \
                         '💶 euro - 15000 uzs\n' + \
                         '💵 dollar - 13500 uzs\n' + \
                         '💷 pound - 14492 uzs', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, exchange)
    else:
        bot.send_message(message.from_user.id, 'Menu:', reply_markup=currency_button.choice_buttons())
        bot.register_next_step_handler(message, text_message)



def dollar(message):
    if message.text == '💵 100$':
        x = 100*13500
        bot.send_message(message.from_user.id, f' 100 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, dollar)
    elif message.text == '💵 200$':
        x = 200*13500
        bot.send_message(message.from_user.id, f' 200 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, dollar)
    elif message.text == '💵 500$':
        x = 500*13500
        bot.send_message(message.from_user.id, f' 500 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, dollar)
    elif message.text == '💵 1000$':
        x = 1000*13500
        bot.send_message(message.from_user.id, f' 1000 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, dollar)
    elif message.text == '💵 2000$':
        x = 2000*13500
        bot.send_message(message.from_user.id, f' 2000 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, dollar)
    elif message.text == 'Back':
        bot.send_message(message.from_user.id, 'Выберите валюту: \n' + \
                         '💶 euro - 15000 uzs\n' + \
                         '💵 dollar - 13500 uzs\n' + \
                         '💷 pound - 14492 uzs', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, exchange)
    else:
        bot.send_message(message.from_user.id, 'Menu:', reply_markup=currency_button.choice_buttons())
        bot.register_next_step_handler(message, text_message)


def pound(message):
    if message.text == '💷 100£':
        x = 100*14492
        bot.send_message(message.from_user.id, f' 100 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, pound)
    elif message.text == '💷 200£':
        x = 200*14492
        bot.send_message(message.from_user.id, f' 200 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, pound)
    elif message.text == '💷 500£':
        x = 500*14492
        bot.send_message(message.from_user.id, f' 500 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, pound)
    elif message.text == '💷 1000£':
        x = 1000*14492
        bot.send_message(message.from_user.id, f' 1000 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, pound)
    elif message.text == '💷 2000£':
        x = 2000*14492
        bot.send_message(message.from_user.id, f' 2000 dollar будет равняться {x} uzs')
        bot.register_next_step_handler(message, pound)
    elif message.text == 'Back':
        bot.send_message(message.from_user.id, 'Выберите валюту: \n' + \
                         '💶 euro - 15000 uzs\n' + \
                         '💵 dollar - 13500 uzs\n' + \
                         '💷 pound - 14492 uzs', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, exchange)
    else:
        bot.send_message(message.from_user.id, 'Menu:', reply_markup=currency_button.choice_buttons())
        bot.register_next_step_handler(message, text_message)


bot.polling()
