import os
import telebot

print("hello")
TELEBOT_TOKEN = os.environ['TELEBOT_TOKEN']
bot = telebot.TeleBot(TELEBOT_TOKEN)
print(bot)

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, "Hello")

bot.polling()