from telebot import types

def choice_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)


    wiki_button = types.KeyboardButton('википедия')
    translate_button = types.KeyboardButton('переводчик')

    kb.add(wiki_button, translate_button)

    return kb