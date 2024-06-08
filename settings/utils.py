from bson import ObjectId
from pymongo import MongoClient
import pymongo


def get_mongo_client():
    uri = 'mongodb+srv://nurzhan:qaws1234@cluster0.acxoanx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
    client = pymongo.MongoClient(uri)
    return client


mongo_client = get_mongo_client()
mongo_db = mongo_client['Notify']



def set_settings(user_id, data):
    collection = mongo_db['social_media']
    data['_id'] = ObjectId()  # Generate a new ObjectId for the document
    result = collection.insert_one(data)  # Insert the data into the collection
    return result