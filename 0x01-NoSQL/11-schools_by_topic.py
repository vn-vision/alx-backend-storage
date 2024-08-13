#!/usr/bin/env python3
'''
python that returns the list of school having specific topic
'''

def schools_by_topic(mongo_collection, topic):
    '''
    returns all documents with 'topic'=topic
    '''
    return list(mongo_collection.find({'topics':topic}))
