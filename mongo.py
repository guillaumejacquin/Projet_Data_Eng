import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://guigui:1234@cluster0.eeflg.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

db = cluster["leagueoflegends"]
collection = db["personnageslol"]


post = {"_id" : 0, "name" : "tim", "score": 5}
collection.insert_one(post)