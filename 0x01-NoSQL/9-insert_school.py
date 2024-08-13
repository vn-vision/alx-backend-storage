#!/usr/bin/env python3
'''
inserts a new document in a collection
'''


def insert_school(mongo_collection, **kwargs):
    '''
    returns the new _id
    '''
    res = mongo_collection.insert_one(kwargs)
    return res.inserted_id
