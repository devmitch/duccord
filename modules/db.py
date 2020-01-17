import pymongo

from pymongo import MongoClient


def start():
    client = MongoClient()
    return client


def init(client, name):
    db = client[name]
    return db


def collection_init(db, name):
    collection = db[name]
    return collection


def insert_one(collection, document):
    result = collection.insert_one(document)
    return result


def find_one(collection, query):
    result = collection.find_one(query)
    return result


def find(collection):
    return collection.find()


def update_one(collection, query, update):
    result = collection.update_one(query, update)
    return result


def delete_all(collection):
    result = collection.delete_many({})
    return result
