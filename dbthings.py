import os
import classes
import pymongo
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import tbutils

print("importato")

uri = os.environ['MONGO']
client = MongoClient(uri, server_api=ServerApi('1'))
try:
  pass
  client.admin.command('ping')
  print("Pinged your deployment. You successfully connected to MongoDB!")
  
except Exception as e:
  print(e)
  pass


db = client["bot"]
leggende = db["leggende"]
gruppi = db["gruppi"]
utenti = db["utenti"]


def legendObj(legend):
  if legend:
    result = classes.Legend(legend["_id"], legend["name"], legend["skinline"], legend["role"], legend["image"], legend["sauce"], legend["guesses"])

  else:
    result = None

  return result

def get_legend_by_id(id):
  print(id)
  result = leggende.find_one({"_id": id})
  print(result)
  return legendObj(result)

def get_all_legends():
  result = leggende.find({})
  return [legendObj(legend) for legend in result].remove(None)

def get_legends_by_role(role):
  result = leggende.find({"role": role})
  return [legendObj(legend) for legend in result].remove(None)

def get_legends_by_skinline(skinline):
  result = leggende.find({"skinline": skinline})
  return [legendObj(legend) for legend in result].remove(None)

def get_legends_by_name(name):
  result = leggende.find({"name": name})
  return [legendObj(legend) for legend in result].remove(None)

def get_legends_by_regex(regex):
  result = leggende.find({"name": {"$regex": regex}})
  return [legendObj(legend) for legend in result].remove(None)

def add_legend(legend):
  pass


for i in range(10, 53):
  print(get_legend_by_id(i))



def add_group(_id, title, photo):
  print("aggiungendo")
  group = {
    "_id" : _id,
    "title" : title,
    "photo" : photo,
    "spawned" : False,
    "message_count" : 0,
    "current" : 0,
    "date" : tbutils.get_date()
  }
  
  gruppi.insert_one(group)


def groupObj(group):
  if group:
    result = classes.Group(group["_id"], group["title"], group["photo"], group["spawned"], group["message_count"], group["current"], group["date"])
  else:
    result = None
  return result


def get_group_by_id(id):
  return groupObj(gruppi.find_one({"_id": id}))

def get_all_groups():
  return [groupObj(group) for group in gruppi.find({})].remove(None)

def get_groups_by_title(title):
  return [groupObj(group) for group in gruppi.find({"title": title})].remove(None)

def get_groups_by_regex(regex):
  return [groupObj(group) for group in gruppi.find({"title": {"$regex": regex}})].remove(None)

def get_groups_by_photo(photo):
  return [groupObj(group) for group in gruppi.find({"photo": photo})].remove(None)

def get_groups_by_date(date):
  return [groupObj(group) for group in gruppi.find({"date": date})].remove(None)

def get_groups_by_spawned(spawned):
  return [groupObj(group) for group in gruppi.find({"spawned": spawned})].remove(None)

