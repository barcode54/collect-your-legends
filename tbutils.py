import telebot
import datetime
import time

def new_keyboard():
  return telebot.types.InlineKeyboardMarkup()

def new_button(text, callback_data):
  return telebot.types.InlineKeyboardButton(text, callback_data=callback_data)

def new_url_button(text, url):
  return telebot.types.InlineKeyboardButton(text, url=url)

def new_inline_query_button(text, query):
  return telebot.types.InlineKeyboardButton(text, switch_inline_query=query)

def parse_callback_data(callback_data):
  return callback_data.split(':')

def unix_to_date(unix):
  return datetime.datetime.utcfromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S')

def ping(date):
  return str(datetime.datetime.fromtimestamp(time.time()) - datetime.datetime.utcfromtimestamp(date))

def get_date():
  return str(datetime.datetime.today())

def download_file(bot, file_id, file_name):
  file_info = bot.get_file(file_id)
  downloaded_file = bot.download_file(file_info.file_path)
  with open(file_name, 'wb') as new_file:
    new_file.write(downloaded_file)