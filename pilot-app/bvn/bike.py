from pymongo import MongoClient


mongo_uri = 'mongodb+srv://admin:admin@cluster0-aekow.mongodb.net/test?retryWrites=true'
client = MongoClient(mongo_uri)

bike = client.db

Bikes = bike['bikes']