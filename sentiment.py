from textblob import TextBlob    
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')

col = client['test']['reviews']

with open("reviews.csv", 'r', encoding='utf-8', errors='ignore') as f:
    reviews = f.readlines()
    for review in reviews:
        text = review.split('" "')
        row = []
        for word in text:
            row.append(word.replace(" ", ""))

        rev = ' '.join(row)

        text = TextBlob(rev)
        polarity = text.sentiment.polarity


        document = {
            "review":rev,
            "polarity":polarity,
            }
        
        insert_result = col.insert_one(document)
        print(f"Inserted document ID: {insert_result.inserted_id}")

        
        
        