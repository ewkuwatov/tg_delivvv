import telebot, buttons
import requests
import json

bot = telebot.TeleBot('6379890652:AAHNdHz36uYZtj0p94CF8z3ftuuz11rxjas')

bank_token = json.loads(requests.get('https://cbu.uz/ru/arkhiv-kursov-valyut/json/').content)

amount = 0
usdRate = float(bank_token[0]['Rate'])
euroRate = float(bank_token[1]['Rate'])
rubRate = float(bank_token[2]['Rate'])

@bot.message_handler(commands=['start'])
def main(message):
    print(message.from_user)
    bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name} {message.from_user.last_name}!')
    bot.send_message(message.chat.id, 'Введите сумму:')
    bot.register_next_step_handler(message, get_but)


@bot.message_handler(commands=['button'])
def get_but(message):
    global amount
    try:
        amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Неверный формат. Впишите сумму.')
        bot.register_next_step_handler(message, get_but)
        return

    if amount > 100:
        bot.reply_to(message, 'Выберите валюту:', reply_markup=buttons.get_mess())
    else:
        bot.send_message(message.chat.id, 'Введеная сумма должна быть больше 100. Впишите сумму заново.')
        bot.register_next_step_handler(message, get_but)

@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'usd':
        print(usdRate)
        res = amount / usdRate
        bot.send_message(callback.message.chat.id, f'{amount} сум будет равняться {round(res, 2)}$')
        bot.register_next_step_handler(callback.message, get_but)
    elif callback.data == 'rub':
        print(rubRate)
        res = amount / rubRate
        bot.send_message(callback.message.chat.id, f'{amount} сум будет равняться {round(res, 2)}RUB')
        bot.register_next_step_handler(callback.message, get_but)
    elif callback.data == 'euro':
        print(euroRate)
        res = amount / euroRate
        bot.send_message(callback.message.chat.id, f'{amount} сум будет равняться {round(res, 2)}EUR')
        bot.register_next_step_handler(callback.message, get_but)


bot.polling()