import pymongo
import os

from os import path
if path.exists("env.py"):
    import env 



MONGODB_URI = os.environ.get("MONGODB_URI")
#SECRET_KEY = os.environ.get("SECRET_KEY")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

documents = coll.find()

for doc in documents:
    print(doc)