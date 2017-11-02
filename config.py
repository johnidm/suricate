import os
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)

load_dotenv(dotenv_path, verbose=True)

# Connection string format to conect on MongoDB
# Example: MONGO_DB_URL=mongodb://localhost:27020/mydb
MONGO_DB_URL= os.getenv('MONGO_DB_URL')

# OAuth access token to connect to the Twitter Streaming API
# https://developer.twitter.com/en/docs/basics/authentication/overview/oauth
TWITTER_CONSUMER_KEY= os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET= os.getenv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN= os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET= os.getenv('TWITTER_ACCESS_TOKEN_SECRET')
