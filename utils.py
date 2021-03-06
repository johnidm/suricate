import csv
import re
import time

import click
from jinja2 import Environment, FileSystemLoader
from functools import reduce
import operator
import config

REGEX_RETWEETED = r'RT @(.+):'
REGEX_BOT_BY_NAME = r'\w{5,}\d{5,}'
REGEX_HTML_TAG = '<[^<>]+>'

__version__ = '0.0.2'


def match(r, t): return bool(re.search(r, t))


def extract_html_tag(t): return re.sub(REGEX_HTML_TAG, '', t)


def flat_list(data):
    return reduce(operator.concat, data)


def save_to_html(data, template_name):

    env = Environment(
        autoescape=False,
        loader=FileSystemLoader('./templates'),
        trim_blocks=False)

    template = env.get_template(f'{template_name}.html')
    output = template.render(data=data)

    filename = __generate_file_name('html')

    with open(filename, 'w') as f:
        f.write(output)

    click.echo(f'Salvando dados em {filename}')


def save_to_csv(data):

    filename = __generate_file_name('csv')

    fieldnames = list(data[0].keys())

    with open(filename, 'w') as f:
        wr = csv.DictWriter(f, fieldnames)
        wr.writeheader()
        wr.writerows(data)

    click.echo(f'Salvando dados em {filename}')


def __generate_file_name(extension):
    timestr = time.strftime("%Y%m%d-%H%M%S")
    return f'{config.OUTPUT_FILE_DIRECTORY}{timestr}.{extension}'
