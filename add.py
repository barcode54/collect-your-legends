import os
import pymongo
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.environ['MONGO']
client = MongoClient(uri, server_api=ServerApi('1'))
try:
  pass
  client.admin.command('ping')
  print("Pinged your deployment. You successfully connected to MongoDB!")
  db = client["bot"]
  leggende = db["leggende"]
  print("adding a legend")

except Exception as e:
  print(e)
  pass