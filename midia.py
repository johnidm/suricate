import json
from datetime import datetime

import click
from tweepy import OAuthHandler, Stream
from tweepy.streaming import StreamListener

import config


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
                f'Erro ao coletar os dados - {status}', fg='red', bold=True))

        def on_limit(self, track):
            click.echo(click.style(
                'Limite de leitura atingido', fg='yellow', bold=True))
            return True

        def on_connect(self):
            click.echo(click.style('Conexão iniciada', fg='white', bold=True))

        def on_disconnect(self, notice):
            click.echo(click.style('Conexão fechada', fg='white', bold=True))

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
