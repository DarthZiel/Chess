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
    filt = {"user_id": user_id}

    if collection.find_one(filt):
        # Исправление фильтра для update_one
        result = collection.update_one(filt, {"$set": data})
    else:
        data['user_id'] = user_id  # Убедитесь, что user_id добавлен в новый документ
        data['_id'] = ObjectId()  # Создание нового ObjectId для документа
        result = collection.insert_one(data)  # Вставка данных в коллекцию

    return result


def delete_setting(user_id):
    collection = mongo_db['social_media']
    filt = {"user_id": user_id}
    collection.find_one_and_delete(filt)
