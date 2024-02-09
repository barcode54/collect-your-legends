import os
import telebot

print("bot started")
TELEBOT_TOKEN = os.environ['TELEBOT_TOKEN']
bot = telebot.TeleBot(TELEBOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, "Hello")

@bot.message_handler(content_types=['photo'])
def aa(message):
  print(message.photo[0].file_id)
  bot.d

bot.polling()