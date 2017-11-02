import config 
import json
import pymongo

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

from utils import Colors

from datetime import datetime


client = pymongo.MongoClient(config.MONGO_DB_URL)
db = client.suricate 


class StdOutListener(StreamListener):

    def __init__(self, collection_name):
        self.collection_name = collection_name

    def on_data(self, data):        
        collection = db[self.collection_name]
        collection.insert_one(json.loads(data))

        print(f'{Colors.GREEN}Collected length({len(data)}) - {str(datetime.now())} {Colors.NO_COLOUR}')
        return True

    def on_error(self, status):
        print(f'{Colors.RED}Error status {status} {Colors.NO_COLOUR}')


def collect_twittes(collection_name, keywords):

    print(f'{Colors.GREEN}Starting collect twittes on collection {collection_name} - Keywords: {keywords}{Colors.NO_COLOUR}')
    
    listener = StdOutListener(collection_name)

    auth = OAuthHandler(config.TWITTER_CONSUMER_KEY, config.TWITTER_CONSUMER_SECRET)
    auth.set_access_token(config.TWITTER_ACCESS_TOKEN, config.TWITTER_ACCESS_TOKEN_SECRET)
        
    stream = Stream(auth, listener)
    stream.filter(track=keywords)
