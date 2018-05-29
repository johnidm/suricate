import re
from collections import Counter
import click

from utils import REGEX_RETWEETED, match, save_to_csv, extract_html_tag, flat_list


def apply(cursor, model):

    RULES = {
        'screen-name': get_display_name,
        'text-not-retweeted': get_text_not_retweeted,
        'text-retweeted': get_text_retweeted,
        'text': get_text,
        'hashtags': get_hashtags,
        'devices': get_devices
    }

    data = RULES[model](cursor)

    save_to_csv(data)


def get_devices(data):

    devices_raw = [d['source'] for d in data]

    devices = list(map(extract_html_tag, devices_raw))

    ordered_devices = Counter(devices)

    return [{
        'device': device,
        'count': count,
    } for device, count in ordered_devices.most_common()]


def get_hashtags(data):

    hashtags_raw = list(
        filter(None, [d['entities']['hashtags'] for d in data]))
    hashtags_text = [d['text'] for d in flat_list(hashtags_raw)]

    hashtags = Counter(hashtags_text)

    return [{
        'text': text,
        'count': count,
    } for text, count in hashtags.most_common()]


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
