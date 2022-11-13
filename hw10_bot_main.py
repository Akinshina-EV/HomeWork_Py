import os.path

from telebot import types

from hw10_bot_init import bot
from hw10_bot_log import log
from hw10_bot_utils import (
    add_row_phonebook, create_phonebook, deleted_contact, find_contact,
    read_phonebook,
)

name = ''
surname = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,
                     'Вас приветствует Телефонный справочник!')
    keyboard = types.ReplyKeyboardMarkup()
    key_open = types.KeyboardButton('open')
    key_search = types.KeyboardButton('search')
    key_add = types.KeyboardButton('add')
    key_delete = types.KeyboardButton('delete')
    keyboard.add(key_open, key_search, key_add, key_delete)
    bot.send_message(message.chat.id, text='Выберете пункт Menu.',
                     reply_markup=keyboard)


@bot.message_handler(commands=['open'])
def open_phonebook(message):
    log(message)
    if os.path.exists('phonebook.csv'):
        bot.send_message(message.chat.id, read_phonebook())
    else:
        phonebook = create_phonebook()
        bot.send_message(message.chat.id, phonebook)
        bot.send_message(message.chat.id,
                         'Уппсс. Кажется в справочнике пока нет записей.')


@bot.message_handler(commands=['search'])
def get_find_world(message):
    log(message)
    bot.send_message(message.from_user.id, 'Введите слово для поиска:')
    bot.register_next_step_handler(message, search_contact)


def search_contact(message):
    log(message)
    find = message.text
    msg = find_contact(find)
    if msg:
        bot.send_message(message.from_user.id, msg)
    else:
        bot.send_message(message.from_user.id, 'Контакты не найдены')


@bot.message_handler(commands=['add'])
def get_name(message):
    log(message)
    if not os.path.exists('phonebook.csv'):
        create_phonebook()
    bot.send_message(message.from_user.id, 'Введите имя:')
    bot.register_next_step_handler(message, get_surname)


def get_surname(message):
    log(message)
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введите фамилию:')
    bot.register_next_step_handler(message, get_phone_number)


def get_phone_number(message):
    log(message)
    global surname
    surname = message.text
    bot.send_message(message.from_user.id, 'Введите номер телефона')
    bot.register_next_step_handler(message, add_contact)


def add_contact(message):
    log(message)
    phone_number = message.text
    new_row = add_row_phonebook(name, surname, phone_number)
    new_contact = ' '.join(new_row) + '\n'
    bot.send_message(message.from_user.id, 'Вы добавили контакт:')
    bot.send_message(message.from_user.id, new_contact)


@bot.message_handler(commands=['delete'])
def del_contact(message):
    log(message)
    bot.send_message(message.chat.id,
                     'Введите ID записи, которую хотите удалить:')
    bot.register_next_step_handler(message, delete_contact)


def delete_contact(message):
    log(message)
    id_contact = message.text
    msg = find_contact(id_contact)
    if msg:
        bot.send_message(message.chat.id, 'Вы удалили запись:')
        bot.send_message(message.from_user.id, msg)
    else:
        bot.send_message(message.from_user.id, 'Контакты не найдены')
    deleted_contact(id_contact)


if __name__ == '__main__':
    bot.polling()
