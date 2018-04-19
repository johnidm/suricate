import re

REGEX_RETWEETED = r'RT @(.+):'
REGEX_BOT_BY_NAME = r'\w{5,}\d{5,}'


def match(r, t): return bool(re.search(r, t))


def save_to_csv(data):
    import csv
    import time
    timestr = time.strftime("%Y%m%d-%H%M%S")

    filename = f'{timestr}.csv'

    fieldnames = list(data[0].keys())

    with open(filename, 'w') as f:
        wr = csv.DictWriter(f, fieldnames)
        wr.writeheader()
        wr.writerows(data)

    click.echo(f'Salvando dados em {filename}')
