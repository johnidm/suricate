import click

import report
import rule
from midia import Twitter
from storage import MongoDB


class Suricate():

    def collect(self, tag, keywords):
        click.echo(click.style(
            'Iniciando a coleta de dados', fg='white', bold=True))
        click.echo(click.style(f'  tag: {tag}', fg='white', bold=True))
        click.echo(click.style(
            f'  keywords: {keywords}', fg='white', bold=True))

        meta = {
            'collection_name': tag,
            'keywords': keywords,
        }

        storage = MongoDB(meta)
        midia = Twitter(storage)
        midia.collect(keywords.split(','))

    def report(self, tag, model):

        meta = {
            'collection_name': tag,
        }

        storage = MongoDB(meta)
        data = storage.data()

        report.apply(data, model)

    def rule(self, tag, name):

        meta = {
            'collection_name': tag,
        }

        storage = MongoDB(meta)
        data = storage.data()

        rule.apply(data, name)
