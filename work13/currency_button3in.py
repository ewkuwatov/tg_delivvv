from telebot import types

def choice_buttons():
    kb = types.InlineKeyboardMarkup(row_width=1)

    euro_but = types.InlineKeyboardButton('💶 euro - 15000 uzs', callback_data='but1')
    doll_but = types.InlineKeyboardButton('💵 dollar - 13500 uzs', callback_data='but2' )
    pou_but = types.InlineKeyboardButton('💷 pound - 14492 uzs', callback_data='but3')

    kb.add(euro_but, doll_but, pou_but)

    return kb