from telebot import types

def choice_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    currency_button = types.KeyboardButton('Валюта')
    exchange_button = types.KeyboardButton('Обмен валют')

    kb.add(currency_button, exchange_button)

    return kb