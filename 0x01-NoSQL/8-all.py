#!/usr/bin/env python3
'''
python function that lists all documents in a collection
'''
from pymongo import MongoClient

def list_all(mongo_collection):
    '''
    returns an empty list if no documents in collection

    client = MongoClient()   # establish connection to default host and port

    # select the database to use
    db = client.my_db

    # select collection
    my_collection = db.mongo_collection

    if  my_collection is None:
        return []
    '''
    # return list(mongo_collection.find())
    return [doc for doc in mongo_collection.find()]
