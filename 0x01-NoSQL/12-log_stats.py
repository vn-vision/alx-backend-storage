#!/usr/bin/env python3
'''
Script provides stats about Nginx logs stored in MongoDB.
'''

from pymongo import MongoClient

def print_nginx_request_logs(nginx):
    '''
    Prints statistics about the Nginx logs:
        - Total number of logs
        - Number of logs for each HTTP method (GET, POST, PUT, PATCH, DELETE)
        - Number of logs with method=GET and path=/status
    '''
    # Count total documents in nginx collection
    print(f'{nginx.count_documents({})} logs')

    # Define the methods to check
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']

    print('Methods:')
    for method in methods:
        # Count documents for each method
        count = nginx.count_documents({'method': method})
        print(f'\tmethod {method}: {count}')

    # Count documents with method=GET and path=/status
    status_count = nginx.count_documents({'method': 'GET', 'path': '/status'})
    print(f'{status_count} status check')

def run():
    '''
    Connect to the MongoDB client and run the log stats function.
    '''
    # Connect to the MongoDB server
    client = MongoClient()

    # Access the logs database and the nginx collection
    nginx_collection = client.logs.nginx

    # Print stats about nginx request logs
    print_nginx_request_logs(nginx_collection)

if __name__ == '__main__':
    run()
