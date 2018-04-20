import os

from dotenv import load_dotenv

env_file = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_file):
    load_dotenv(env_file)

# Connection string format to conect on MongoDB
# Example: MONGO_DB_URL=mongodb://localhost:27017/suricate
MONGO_DB_URL = os.getenv('MONGO_DB_URL')

# OAuth access token to connect to the Twitter Streaming API
# https://developer.twitter.com/en/docs/basics/authentication/overview/oauth
# Get Apps - https://apps.twitter.com/
TWITTER_CONSUMER_KEY = os.getenv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET = os.getenv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN = os.getenv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET = os.getenv('TWITTER_ACCESS_TOKEN_SECRET')

# Diretório onde os arquivos gerados serão salvos
# Ex: /Users/Computer/Desktop/suricate/
# A barra no final deve ser incluída
OUTPUT_FILE_DIRECTORY = os.getenv('OUTPUT_FILE_DIRECTORY', '')
