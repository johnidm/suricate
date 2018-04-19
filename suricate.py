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

        storage = MongoDB(tag)
        midia = Twitter(storage)
        midia.collect(keywords.split(','))

    def report(self, tag, model):
        storage = MongoDB(tag)
        data = storage.data()

        report.apply(data, model)

    def rule(self, tag, name):
        storage = MongoDB(tag)
        data = storage.data()

        rule.apply(data, name)
