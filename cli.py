import click

from suricate import Suricate


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Suricate()


@cli.command('collect')
@click.option('--tag', help='Marca os registros recuperados')
@click.option('--keywords', help='Palavras chaves, separadas por ponto e virgula, utilizadas na busca por tuites')
@click.pass_obj
def collect(suricate, tag, keywords):

    if tag is None:
        raise click.BadParameter(
            'É necessário informar uma balor para o parâmetro  "tag". Esse valor é usado para criar uma coleção dos dados coletados', param_hint=['--tag'])

    if keywords is None:
        raise click.BadParameter(
            'É necessário informar as palavras chaves para a busca.', param_hint=['--keywords'])

    suricate.collect(tag, keywords)


@cli.command('extract')
@click.option('--tag', help='Marca os registros recuperados')
@click.option('--rule')
@click.pass_obj
def extract(suricate, tag, rule):

    if rule is None:
        raise click.BadParameter(
            'É necessário informar a regra para extrair os dados', param_hint=['--rule'])

    suricate.extract(tag, rule)
