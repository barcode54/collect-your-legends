import os
import telebot
import dbthings
import time
import tbutils
import json

print("bot started")
TELEBOT_TOKEN = os.environ['TELEBOT_TOKEN']
bot = telebot.TeleBot(TELEBOT_TOKEN, threaded=False)
capo = os.environ['CAPO']

def get_manutenzione():
  with open("cfg.json") as f:
    data = json.loads(f.read())
    f.close()

  manutenzione = bool(data["manutenzione"])
  return manutenzione

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
    id = message.chat.id
    if not dbthings.get_group_by_id(id):
      photo = message.chat.photo.big_file_id
      dbthings.add_group(id, message.chat.title, photo)
      tbutils.download_file(bot, photo, "groups/{}.png".format(id))
      bot.send_message(capo, "i was added to {} !!".format(message.chat.title))
  else:
    bot.reply_to(message, "Hi! {} Welcome to the group !".format(message.new_chat_members[0].first_name))


@bot.message_handler(commands=['info'])
def bot_info(message):
  kb = tbutils.new_keyboard()
  btn1 = tbutils.new_url_button("👤Author", "tg://user?id={}".format(capo))
  btn2 = tbutils.new_url_button("🖥️GitHub", "https://github.com/barcode54")
  btn3 = tbutils.new_url_button("☕buy me a coffee", "https://herta.eu.org/")
  kb.row(btn1, btn2, btn3)
  
  bot.reply_to(message, "👋 (please pretend im writing something useful and intelligent idk what to say)\nto protecc legend use\n\n/protecc <name> (without the <> of course)", reply_markup=kb)



while 1:
  try:
    bot.polling(non_stop=False)
  except Exception as e:
    print(e)

  time.sleep(3)