import pandas as pd
import json

data = pd.read_json("final.json")
df1 = data[data["remarquable"] == "OUI"]
colonnes = [
    "idbase",
    "typeemplacement",
    "domanialite",
    "arrondissement",
    "complementadresse",
    "adresse",
    "idemplacement",
    "libellefrancais",
    "genre",
    "espece",
    "varieteoucultivar",
    "circonferenceencm",
    "hauteurenm",
    "stadedeveloppement",
    "remarquable",
    "geo_point_2d",
]

df1 = df1[colonnes]

#Merge lat lon
df1["lat"] = df1["geo_point_2d"].apply(lambda x: x["lat"])
df1["lon"] = df1["geo_point_2d"].apply(lambda x: x["lon"])
df1 = df1.drop(columns=["geo_point_2d"])

print(df.info())
