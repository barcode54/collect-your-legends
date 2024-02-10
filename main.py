import os
import telebot
import dbthings
import time
import tbutils

print("bot started")
TELEBOT_TOKEN = os.environ['TELEBOT_TOKEN']
bot = telebot.TeleBot(TELEBOT_TOKEN, threaded=False)

@bot.message_handler(commands=['start'], chat_types=['private'])
def start(message):
  kb = tbutils.new_keyboard()
  add_button = tbutils.new_url_button("➕ add me a group", "https://t.me/collect_your_legends_bot?startgroup=start")
  kb.add(add_button)
  
  bot.reply_to(message, "_\"her eyes were a portrait of a world without my cruelty\.\.\.\"_", reply_markup=kb, parse_mode="MARKDOWNV2")


@bot.message_handler(commands=['ping'])
def ping(message):
  response = tbutils.ping(message.date)
  bot.reply_to(message, "🏓 pong! \n\n<code>{}s</code>".format(response[6:-3:]), parse_mode='HTML')


@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
  if message.new_chat_members[0].username == 'collect_your_legends_bot':
    bot.reply_to(message, "Thank you for adding me !")
    
  else:
    bot.reply_to(message, "Hi! {} Welcome to the group !".format(message.new_chat_members[0].first_name))



while 1:
  try:
    bot.polling(non_stop=False)
  except Exception as e:
    print(e)

  time.sleep(3)