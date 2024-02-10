import os
import pymongo
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import dbthings

uri = os.environ['MONGO']
client = MongoClient(uri, server_api=ServerApi('1'))
try:
  pass
  client.admin.command('ping')
  print("Pinged your deployment. You successfully connected to MongoDB!")
  db = client["bot"]
  #leggende = db["leggende"]
  #print("adding a legend")
  #all = dbthings.get_all_legends()
  #a = all[0]._id
  #print(a, type(a))
  #print(leggende.find_one({"_id": a}))
  #leggende.update_one({"_id": a}, { "$set": {"_id" : 1}})
  #print(leggende.find_one({"_id": 1}))

except Exception as e:
  print(e)
  pass