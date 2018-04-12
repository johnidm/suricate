import os

from dotenv import load_dotenv

env_file = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_file):
    load_dotenv(env_file)

# Connection string format to conect on MongoDB
# Example: MONGO_DB_URL=mongodb://localhost:27020/mydb
MONGO_DB_URL = os.getenv('MONGO_DB_URL')

# OAuth access token to connect to the Twitter Streaming API
# https://developer.twitter.com/en/docs/basics/authentication/overview/oauth
TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
