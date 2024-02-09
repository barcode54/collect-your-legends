import os
import telebot

print("bot started")
TELEBOT_TOKEN = os.environ['TELEBOT_TOKEN']
bot = telebot.TeleBot(TELEBOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, "Hello")

i = 9
@bot.message_handler(content_types=['photo'])
def aa(message):
  print(message.photo[0].file_id)
  print(message.caption)
  file = bot.get_file(message.photo[0].file_id)
  downloaded = bot.download_file(file.file_path)
  with open("images/jojo.png", 'wb') as new_file:
    new_file.write(downloaded)

  i = i+1


bot.polling("images")