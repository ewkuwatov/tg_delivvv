from telebot import types

def get_mess():
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('USD', callback_data='usd')
    markup.row(btn1)
    btn2 = types.InlineKeyboardButton('RUB', callback_data='rub')
    btn3 = types.InlineKeyboardButton('EURO', callback_data='euro')
    markup.row(btn2, btn3)

    return markup