#!/usr/bin/env python3
'''
script provides stats about nginx los stored in MongoDB
'''

from pymongo import MOngoClient


def print_nginx_request_logs(nginx):
    '''
    Database: logs
    Collection: nginx
    Display (same as the example):
        first line: x logs where x is the number of documents in this collection
        second line: Methods:
        5 lines with the number of documents with the method = ["GET", "POST", "PUT", "PATCH", "DELETE"] in this order (see example below - warning: it’s a tabulation before each line)
        one line with the number of documents with:
            method=GET
            path=/status
    '''

    # count documens in nginx collection
    print('{} logs'.format(nginx.count_documents({})))

    print('Methods:')

    # methods in the collection
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:  # get records for each method
        count = len(list(nginx.find({'method':method})))
        print('\tmethod {} : {}'.format(method, count))

    status_count = len(list(nginx.find({'method':'GET', 'path':'/status'})))

    print('{} status check'.format(status_count))


def run():
    '''
    run the mongo client with passed collection
    '''

    client = MongoClient()
    print_nginx_request_logs(client.logs.nginx)


if __name__ = '__main__':
    run()
