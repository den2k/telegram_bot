import telebot

API_TOKEN = '7954921965:AAGUz4SIIFiO0Y6yh04ICz0-6j3v1Vmo8es'
bot = telebot.TeleBot(API_TOKEN)

@bot.message_handler(commands = ['start'])
def start(message):
    bot.send_message(message.chat.id, 'Здарова ебать!\nЧе опять надо?')

@bot.message_handler(commands = ['bullshit'])
def start(message):
    bot.send_message(message.chat.id, 'На кого быкануть?')

bot.polling(none_stop=True)

