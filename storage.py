
import pymongo

import config
import statistic


class MongoDB():

    def __init__(self, collection_name):
        client = pymongo.MongoClient(config.MONGO_DB_URL)
        db = client.suricate
        self.collection = db[collection_name]

    def insert(self, json):
        self.collection.insert_one(json)

    def query(self, rule):
        cursor = list(self.collection.find({}))
        statistic.apply_rule(cursor, rule)
