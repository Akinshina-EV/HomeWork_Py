import datetime


def log(message):
    dtn = datetime.datetime.now()
    with open('Calc_bot_log.csv', 'a') as log_file:
        log_file.write(f'{dtn}, Пользователь, {message.from_user.first_name}, '
                       f'{message.from_user.id}, запросил вычисление '
                       f'следующего арифметического выражения: '
                       f'{message.text}\n')
