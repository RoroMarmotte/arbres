import json

files = [
    "premier.json",
    "second.json"
]

merged = []

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

        if isinstance(data, list):
            merged.extend(data)
        else:
            merged.append(data)

# Écriture du résultat unifié
with open("final.json", "w", encoding="utf-8") as f:
    json.dump(merged, f, indent=2, ensure_ascii=False)

print("JSON unifié créé dans final.json")
