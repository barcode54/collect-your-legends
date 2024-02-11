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




def avvisa(avviso):
  bot.send_message(capo, avviso)

def is_capo(id):
  if str(id) == str(capo):
    return True

  else:
    return False

def get_manutenzione(id):
  with open("cfg.json", 'r') as f:
    data = json.loads(f.read())
    f.close()

  if is_capo(id):
    manutenzione = False

  else:
    manutenzione = bool(data["manutenzione"])
  return manutenzione 


def manutenzione_on(bot):
  with open("cfg.json", "w") as f:
    data = {"manutenzione": 1}
    f.write(json.dumps(data))
    f.close()

  bot.set_my_name("[OFF]𝐂𝐨𝐥𝐥𝐞𝐜𝐭 𝐘𝐨𝐮𝐫 𝐋𝐞𝐠𝐞𝐧𝐝𝐬")
  return


def manutenzione_off(bot):
  with open("cfg.json", "w") as f:
    data = {"manutenzione": 0}
    f.write(json.dumps(data))
    f.close()

  bot.set_my_name("𝐂𝐨𝐥𝐥𝐞𝐜𝐭 𝐘𝐨𝐮𝐫 𝐋𝐞𝐠𝐞𝐧𝐝𝐬")
  return


avvisa("bot startato!")


@bot.message_handler(commands=['start'], chat_types=['private'])
def start(message):
  kb = tbutils.new_keyboard()
  add_button = tbutils.new_url_button("➕ add me a group", "https://t.me/collect_your_legends_bot?startgroup=start")
  kb.add(add_button)
  
  bot.reply_to(message, "_\"her eyes were a portrait of a world without my cruelty\.\.\.\"_", reply_markup=kb, parse_mode="MARKDOWNV2")


@bot.message_handler(commands=['on'], chat_types=['private'], func=lambda message : is_capo(message.from_user.id))
def rompi(message):
  manutenzione_off(bot)
  bot.reply_to(message, "il bot è nuovamente in funzione!\n\nmanutenzione: Disattivata\nstato: ON")


@bot.message_handler(commands=['off'], chat_types=['private'], func=lambda message : is_capo(message.from_user.id))
def ripristina(message):
  manutenzione_on(bot)
  bot.reply_to(message, "il funzionamento del bot è sospeso.\n\nmanutenzione: Attiva\nstato: OFF")


@bot.message_handler(commands=['ping'], func=lambda message : not get_manutenzione(id))
def ping(message):
  response = tbutils.ping(message.date)
  bot.reply_to(message, "🏓 pong! \n\n<code>{}s</code>".format(response[6:-3:]), parse_mode='HTML')


@bot.message_handler(content_types=['new_chat_members'])
def welcome(message):
  if message.new_chat_members[0].username == 'collect_your_legends_bot':
    bot.reply_to(message, "Thank you for adding me !")
    id = message.chat.id
    if not dbthings.get_group_by_id(id):
      print(message)
      photo = bot.get_chat(id).photo
      if not photo:
        path = "groups/default.png"
      else:
        path = "groups/{}.png".format(id)
        photo = photo.big_file_id
      dbthings.add_group(id, message.chat.title, path)
      tbutils.download_file(bot, photo, path)
      bot.send_message(capo, "i was added to {} !! ({})".format(message.chat.title, id))
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
    avvisa("an error occured: {}".format(e))

  time.sleep(3)