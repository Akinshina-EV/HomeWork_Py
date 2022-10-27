import telebot

with open('bot_token.txt', 'r') as file:
    token = file.read()

bot = telebot.TeleBot(token)
