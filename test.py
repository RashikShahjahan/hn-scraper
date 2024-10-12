
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

col = client['restaurants']['reviews']
for doc in col.find():
    print(doc["polarity"])
