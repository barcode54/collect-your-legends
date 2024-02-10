import os
import telebot
import dbthings

print("bot started")
TELEBOT_TOKEN = os.environ['TELEBOT_TOKEN']
bot = telebot.TeleBot(TELEBOT_TOKEN, threaded=False)

@bot.message_handler(commands=['start'])
def start(message):
  bot.reply_to(message, "Hello")

i = 10
@bot.message_handler(content_types=['photo'])
def aa(message):
  global i
  leggenda = dbthings.get_legend_by_id(i)
  print("editando", leggenda.name, i)
  print(leggenda.name)
  print(message.photo[0].file_id)
  print(message.caption)
  file = bot.get_file(message.photo[0].file_id)
  downloaded = bot.download_file(file.file_path)
  with open("images/{}.png".format(leggenda.name).lower(), 'wb') as new_file:
    new_file.write(downloaded)
    new_file.close()

  dbthings.editalo(i, message.caption)

  i = i+1


bot.polling()