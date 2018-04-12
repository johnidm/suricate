import click

from midia import Twitter
from storage import MongoDB


class Suricate():

    def collect(self, tag, keywords):
        click.echo(click.style(
            'Iniciando a coleta de dados', fg='white', bold=True))
        click.echo(click.style(f'  tag: {tag}', fg='white', bold=True))
        click.echo(click.style(
            f'  keywords: {keywords}', fg='white', bold=True))

        storage = MongoDB(tag)
        midia = Twitter(storage)
        midia.collect(keywords.split(','))

    def extract(self, tag, rule):
        storage = MongoDB(tag)
        storage.query(rule)
