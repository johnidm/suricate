
import pymongo

import config


class MongoDB():

    def __init__(self, collection_name):
        client = pymongo.MongoClient(config.MONGO_DB_URL)
        db = client.suricate
        self.collection = db[collection_name]

    def insert(self, json):
        self.collection.insert_one(json)

    def data(self):
        return list(self.collection.find({}))
