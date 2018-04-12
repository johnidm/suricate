import re

import click


def apply_rule(cursor, rule):
    data = RULES[rule](cursor)

    save_to_csv_file(data)

    return data


def save_to_csv_file(data):
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


REGEX_RETWEETED = r'RT @(.+):'


def match(r, t): return bool(re.search(r, t))


def get_display_name(data):

    return [{
        'username': d['user']['screen_name']
    } for d in data]


def get_text(data):

    return [{
        'id': d['id_str'],
        'text': d['text'],
    } for d in data]


def get_text_not_retweeted(data):
    texts = get_text(data)
    return [t for t in texts if not match(REGEX_RETWEETED, t[1])]


def get_text_retweeted(data):
    texts = get_text(data)
    return [t for t in texts if match(REGEX_RETWEETED, t[1])]


RULES = {
    'screen-name': get_display_name,
    'text-not-retweeted': get_text_not_retweeted,
    'text-retweeted': get_text_retweeted,
    'text': get_text,
}
