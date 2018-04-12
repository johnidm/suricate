from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from datetime import datetime
import config


class Twitter():

    class StdOutListener(StreamListener):

        def __init__(self, storage):
            self.storage = storage

        def on_data(self, data):
            storage.insert(json.loads(data))

            click.echo(click.style(
                f'Tamanho do retorno({len(data)}) - {str(datetime.now())}', fd='greem'))

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
