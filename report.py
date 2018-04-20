import re

import click

from utils import REGEX_RETWEETED, match, save_to_csv


def apply(cursor, model):

    RULES = {
        'screen-name': get_display_name,
        'text-not-retweeted': get_text_not_retweeted,
        'text-retweeted': get_text_retweeted,
        'text': get_text,
    }

    data = RULES[model](cursor)
    save_to_csv(data)


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
    return [t for t in texts if not match(REGEX_RETWEETED, t['id'])]


def get_text_retweeted(data):
    texts = get_text(data)
    return [t for t in texts if match(REGEX_RETWEETED, t['text'])]
