from storage import MongoDB
from midia import Twitter
import click


class Suricate():

    def collect(self, tag, keywords):
        click.echo(click.style('Iniciando a coleta de dados'))
        click.echo(click.style(f'  tag: {tag}', fg='blue'))
        click.echo(click.style(f'  keywords: {keywords}', fg='blue'))

        storage = MongoDB(tag)
        midia = Twitter(storage)
        midia.collect(keywords.split(','))

    def statistics(self):
        pass

