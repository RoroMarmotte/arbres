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
'''
for nom in noms_arbres:
    list_arbres.append(nom)
    print(nom)
'''
#Phase 4 

#Lister les  10 premier arbre sud bois de vincenne

arbres_vincennes = collection.find({"commune":"BOIS DE VINCENNES"}, {"_id": 0, "nom":1}).limit(10)
'''
for arbre in arbres_vincennes:
    print(arbre)
'''

#Lister les les arbres de plus de 20 metres de hauteur
arbres_hauts = collection.find({"hauteur": {"$gt": 20}}, {"_id": 0, "nom":1, "hauteur":1})
'''
for arbre in arbres_hauts:
    print(arbre)
'''
#Lister les arbres qui contiennent le nom "Chêne"


arbres_chene = collection.find({"nom": {"$regex":"Chêne"}},{"_id": 0, "nom":1})
'''
for arbre in arbres_chene:
    print(arbre)
'''
# Lister les arbres les plus hauts (10 premiers)

arbres_higer = collection.find({"commune":"BOIS DE BOULOGNE"},{"_id": 0, "nom":1,"commune":1, "hauteur":1}).limit(10).sort("hauteur",-1)
'''
for arbre in arbres_higer:
    print(arbre)
'''

#Lister les arbres avec circonference connue et > 3 metres 
arbres_circonferce = collection.find({"circonference": {"$gt":3,"$ne": None}},{"_id":0,"nom":1,"circonference":1}).sort("circonference",-1)

'''
for arbre in arbres_circonferce:
    print(arbre)
'''

#Nombre d'arbre par commune 

count_per_commune = collection.aggregate([
    {
        "$group": {
            "_id": "$commune",
            "nb_arbres": {"$sum": 1}
        }
    }
])

