import os
import classes
import pymongo
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
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


def legendObj(legend):
  return classes.Legend(legend["_id"], legend["name"], legend["skinline"], legend["role"], legend["image"], legend["sauce"], legend["guesses"])

def get_legend_by_id(id):
  print(id)
  result = leggende.find_one({"_id": id})
  print(result)
  return legendObj(result)

def get_all_legends():
  result = leggende.find({})
  return [legendObj(legend) for legend in result]

def get_legends_by_role(role):
  result = leggende.find({"role": role})
  return [legendObj(legend) for legend in result]

def get_legends_by_skinline(skinline):
  result = leggende.find({"skinline": skinline})
  return [legendObj(legend) for legend in result]

def get_legends_by_name(name):
  result = leggende.find({"name": name})
  return [legendObj(legend) for legend in result]

def get_legends_by_regex(regex):
  result = leggende.find({"name": {"$regex": regex}})
  return [legendObj(legend) for legend in result]

def add_legend(legend):
  pass

def editalo(_id, sauce):
  q = {"_id" : _id}
  leggende.update_one(q, {"$set" : {"sauce" : sauce}})


print(get_legend_by_id(9).sauce)