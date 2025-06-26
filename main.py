from pymongo import MongoClient
from pymongo.errors import ConnectionFailure


# CONNESSIONE AL DB
mongoConnection = input("Incolla qui la stringa per la connessione a Mongo: ").strip()

while True:
    try:
        client = MongoClient(mongoConnection)
        client.admin.command('ping')
        print("Connessione avvenuta con successo")
        break
    except ConnectionFailure:
        print("Connessione fallita. Controlla la stringa di connessione.")
        continue


# VISUALIZZAZIONE DI TUTTI I DATABASE
allDb = client.list_database_names()

for db in allDb:
    print(db)

while True:
    dbName = input("Inserisci il nome del database: [ATTENZIONE ALLE MAIUSCOLE/MINUSCOLE]: ").strip()
    if dbName not in allDb:
        print("Nome database non corretto")
    else: break

db = client[dbName]

collections = db.list_collection_names()

if collections:
    print(f"Queste sono le tue collezioni: {collections}")
else:
    print(f"Non sono presenti collezioni nel database: {dbName}")
    exit()

singleCollection = input("Inserisci il nome esatto della collezione da visualizzare: ").strip()

collection = db[singleCollection]
docs = list(collection.find())

if docs:
    for doc in docs:
        print("Documento:")
        for chiave, valore in doc.items():
            print(f"  {chiave}: {valore}")
        print("-" * 30)
        

else:
    print(f"Non sono presenti documenti nella collezione: {singleCollection}")

