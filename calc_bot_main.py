from calc_bot_init import bot
from calc_bot_log import log


@bot.message_handler(commands=['start'])
def start_message(message):
    start_text = f'Привет, {message.from_user.first_name}! Что будем ' \
                 f'вычислять?\nВведите арифметическое выражение из чисел и ' \
                 f'операторов.'
    bot.send_message(message.chat.id, start_text)


@bot.message_handler(content_types=['text'])
def eval_command(message):
    log(message)
    expression = message.text
    try:
        eval(expression)
    except (SyntaxError, NameError):
        bot.send_message(message.chat.id,
                         f'Вы ввели некорректное выражение.\nАрифметическое '
                         f'выражение может содержать только числа и '
                         f'арифметические операторы.')
    else:
        bot.send_message(message.chat.id,
                         f'Результат выражения равен:\n{eval(expression)}')


if __name__ == '__main__':
    bot.polling()
