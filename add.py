import os
import pymongo
from bson.objectid import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.environ['MONGO']
client = MongoClient(uri, server_api=ServerApi('1'))
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
    db = client["bot"]
    leggende = db["leggende"]
    print("adding a legend")
    name = input("name: ")
    skinline = input("skinline: ")
    role = input("role: ")
    image = input("image: ")
    sauce = input("sauce: ")
    id = len([i for i in leggende.find({})])+1
  
    leggenda = {"name" : name, "skinline" : skinline, "role" : role, "image" : image, "sauce" : sauce, "_id" : id}

    leggende.insert_one(leggenda)
    lista = [i for i in leggende.find({})]
    print(lista)
except Exception as e:
    print(e)