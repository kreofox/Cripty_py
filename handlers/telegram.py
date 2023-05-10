import telebot

def send_notify(message):
    bot = telebot.TeleBot('TOKEN')
    bot.send.message(1798624919, message)