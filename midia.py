from datetime import datetime

from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

import config
import json
import click


class Twitter():

    class StdOutListener(StreamListener):

        def __init__(self, storage):
            self.storage = storage

        def on_data(self, data):
            self.storage.insert(json.loads(data))

            click.echo(click.style(
                f'Tamanho do retorno({len(data)}) - {str(datetime.now())}', fg='white', bold=True))

            return True

        def on_error(self, status):
            click.echo(click.style(
                f'Erro ao coletar os dados - {status}', fd='red', bold=True))

    def __init__(self, storage):
        self.storage = storage

    def collect(self, keywords):

        listener = Twitter.StdOutListener(self.storage)
        auth = OAuthHandler(config.TWITTER_CONSUMER_KEY,
                            config.TWITTER_CONSUMER_SECRET)
        auth.set_access_token(config.TWITTER_ACCESS_TOKEN,
                              config.TWITTER_ACCESS_TOKEN_SECRET)

        stream = Stream(auth, listener)
        stream.filter(track=keywords)
