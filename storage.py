
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

        metadata = {
            'collected_date': datetime.now(),
        }

        metadata.update(self.meta)

        one = {
            'data': data,
            'metadata': metadata
        }

        self.collection.insert_one(one)

    def data(self):
        return list(self.collection.find({}))
