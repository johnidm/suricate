import pymongo
import config


class MongoDB():

    def __init__(self, collection_name):
        self.collection_name = collection_name

        client = pymongo.MongoClient(config.MONGO_DB_URL)
        self.db = client.suricate

    def insert(self, json):
        collection = self.db[self.collection_name]
        collection.insert_one(json)
