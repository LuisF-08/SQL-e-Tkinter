from pymongo import MongoClient
from pprint import pprint

client = MongoClient()

mydb = client.dbposts
mycol = mydb.posts

#retorn todos os documentos
result = mycol.find()

print("Lista de posts:")
for r in result:
    pprint(r)