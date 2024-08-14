#!/usr/bin/env python3
'''
redis
'''

import redis
import uuid


class Cache:
    '''
    blueprint for redis cache: store, get, set, ...
    '''

    def __init__(self):
        '''
        class constructor
        '''
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data):
        '''
        takes data argument and returns string
        '''
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key, fn=None):
        '''
        takes a string arg and an optional callable
        The callable will convert the data to desired format
        '''
        data = self._redis.get(key)
        if data is None:
            return None

        if fn is not None:
            return fn(data)

        return data

    def get_str(self, key):
        '''
        Retrieve the data and convert to UTF-8 string
        '''
        return self.get(key, fn=lambda d: d.decode("UTF-8"))

    def get_int(self, key):
        '''
        Retrieve the data and convert to int
        '''
        return self.get(key, fn=int)

