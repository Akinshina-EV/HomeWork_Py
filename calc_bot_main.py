import telebot

from calc_bot_log import log

with open('bot_token.txt', 'r') as file:
    token = file.read()

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_message(message):
    start_text = f'Привет, {message.from_user.first_name}! Что будем ' \
                 f'вычислять?\nВведите арифметическое выражение.'
    bot.send_message(message.chat.id, start_text)


@bot.message_handler(content_types=['text'])
def eval_command(message):
    log(message)
    expression = message.text
    bot.send_message(message.chat.id,
                     f'Результат выражения равен:\n{eval(expression)}')


bot.polling()
