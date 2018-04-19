import click

from suricate import Suricate


@click.group()
@click.pass_context
def cli(ctx):
    ctx.obj = Suricate()


@cli.command()
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


@cli.command()
@click.option('--tag', help='Marca os registros recuperados')
@click.option('--model')
@click.pass_obj
def report(suricate, tag, model):

    if model is None:
        raise click.BadParameter(
            'É necessário informar um modelo para extrair os dados', param_hint=['--model'])

    suricate.report(tag, model)


@cli.command()
@click.option('--tag', help='Marca os registros recuperados')
@click.option('--name')
@click.pass_obj
def rule(suricate, tag, name):

    if name is None:
        raise click.BadParameter(
            'É necessário informar o nome da regra a ser aplicada.', param_hint=['--name'])

    suricate.rule(tag, name)
