from config import MONGO_CONFIG
from pymongo import MongoClient

client = MongoClient(
    host="localhost",
    port=27017,
    username="root",
    password="root",
    authSource="admin"
)

collection = client["arbres"]["arbres"]
noms_arbres = collection.distinct("nom")
list_arbres = []
for nom in noms_arbres:
    list_arbres.append(nom)
    print(nom)