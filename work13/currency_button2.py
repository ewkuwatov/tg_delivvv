from telebot import types

def cur_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    hundret_button = types.KeyboardButton('💶 100 euro')
    twohundret_button = types.KeyboardButton('💶 200 euro')
    fivehundret_button = types.KeyboardButton('💶 500 euro')
    thousand_button = types.KeyboardButton('💶 1000 euro')
    twothousand_button = types.KeyboardButton('💶 2000 euro')
    back = types.KeyboardButton('Back')
    menu = types.KeyboardButton('Menu')


    kb.add(hundret_button, twohundret_button, fivehundret_button, thousand_button, twothousand_button, back, menu)

    return kb

def cur_buttons2():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    hundret_button = types.KeyboardButton('💵 100$')
    twohundret_button = types.KeyboardButton('💵 200$')
    fivehundret_button = types.KeyboardButton('💵 500$')
    thousand_button = types.KeyboardButton('💵 1000$')
    twothousand_button = types.KeyboardButton('💵 2000$')
    back = types.KeyboardButton('Back')
    menu = types.KeyboardButton('Menu')

    kb.add(hundret_button, twohundret_button, fivehundret_button, thousand_button, twothousand_button, back, menu)

    return kb

def cur_buttons3():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    hundret_button = types.KeyboardButton('💷 100£')
    twohundret_button = types.KeyboardButton('💷 200£')
    fivehundret_button = types.KeyboardButton('💷 500£')
    thousand_button = types.KeyboardButton('💷 1000£')
    twothousand_button = types.KeyboardButton('💷 2000£')
    back = types.KeyboardButton('Back')
    menu = types.KeyboardButton('Menu')

    kb.add(hundret_button, twohundret_button, fivehundret_button, thousand_button, twothousand_button, back, menu)

    return kb

