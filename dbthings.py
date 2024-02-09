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
    print(db)
    print(client.list_database_names())
    print(db.list_collection_names())

    leggenda = {"name" : "Ahri", "skinline" : "base", "role" : "mid", "image" : "images/ahri.png", "sauce" : "https://www.pixiv.net/en/artworks/105621558", "_id" : "2"}
    x = leggende.insert_one(leggenda)
    print(x.inserted_id)
    lista = [i for i in leggende.find({})]
    print(lista)
except Exception as e:
    print(e)