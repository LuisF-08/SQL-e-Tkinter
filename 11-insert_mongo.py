from pymongo import MongoClient

client = MongoClient()
mydb = client.dbposts
mycol = mydb.posts

post1 = {
    "title": "Pandas",
    "category": "Data Analysis",
    "level": "Intermediário",
    "author": {
        "name": "Luís",
        "email": "luis@email.com"
    }
}

result = mycol.insert_one(post1)
print("Post inserido com o id:", result.inserted_id)