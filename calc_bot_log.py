import datetime


def log(message):
    dtn = datetime.datetime.now()
    log_file = open('Calc_bot_log.csv', 'a')
    log_file.write(f'{dtn}, Пользователь, {message.from_user.first_name}, '
                   f'{message.from_user.id}, запросил вычисление следующего '
                   f'арифметического выражения: {message.text}\n')
    log_file.close()
