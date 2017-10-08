import os


# Connection string format to conect on MongoDB
# Example: MONGO_DB_URL=mongodb://localhost:27020/mydb
MONGO_DB_URL= os.getemv('MONGO_DB_URL')

# OAuth access token to connect to the Twitter Streaming API
# https://developer.twitter.com/en/docs/basics/authentication/overview/oauth
TWITTER_CONSUMER_KEY= os.getemv('TWITTER_CONSUMER_KEY')
TWITTER_CONSUMER_SECRET= os.getemv('TWITTER_CONSUMER_SECRET')
TWITTER_ACCESS_TOKEN= os.getemv('TWITTER_ACCESS_TOKEN')
TWITTER_ACCESS_TOKEN_SECRET= os.getemv('TWITTER_ACCESS_TOKEN_SECRET')
