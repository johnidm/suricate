
from datetime import datetime

import pymongo

import config


class MongoDB():

    def __init__(self, meta):
        client = pymongo.MongoClient(config.MONGO_DB_URL)
        db = client.suricate
        self.collection = db[meta['collection_name']]
        self.meta = meta

    def insert(self, data):
        one = {
            'data': data,
            'metadata': {
                'date': datetime.now(),
                'keywords': self.meta['keywords']
                # 'computer_name': 'johni-pc',
                'computer_ip': self.__get_ip()
            }
        }

        self.collection.insert_one(one)

    def data(self):
        return list(self.collection.find({}))

    def __get_ip(self):
        import socket
        return socket.gethostbyname(socket.gethostname())
