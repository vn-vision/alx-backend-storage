#!/usr/bin/env python3
'''
Script provides stats about Nginx logs stored in MongoDB.
'''

from pymongo import MongoClient

def print_nginx_request_logs(nginx):
    '''
    Database: logs
    Collection: nginx
    Displays the statistics:
        - First line: x logs where x is the number of documents in this collection.
        - Second line: Methods:
        - 5 lines with the number of documents with the method in ["GET", "POST", "PUT", "PATCH", "DELETE"].
        - One line with the number of documents with:
            method=GET
            path=/status
    '''

    # Count documents in nginx collection
    print('{} logs'.format(nginx.count_documents({})))

    print('Methods:')

    # Methods in the collection
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    for method in methods:  # Get records for each method
        count = nginx.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, count))

    # Count the documents where method is GET and path is /status
    status_count = nginx.count_documents({'method': 'GET', 'path': '/status'})
    print('{} status check'.format(status_count))

def run():
    '''
    Run the MongoDB client with the passed collection.
    '''
    client = MongoClient()
    print_nginx_request_logs(client.logs.nginx)

if __name__ == '__main__':
    run()
