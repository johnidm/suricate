import itertools
from difflib import SequenceMatcher

from utils import REGEX_BOT_BY_NAME, REGEX_RETWEETED, match, save_to_html


def apply(data, name):

    RULES = {
        'check-similarity': check_similarity,
        'bot-by-name': bot_by_name,
    }

    RULES[name](data)


def check_similarity(data):

    def similar(a, b):
        ratio = SequenceMatcher(None, a, b).ratio()
        return ratio

    def check_similarity(a, b):
        return a, b, similar(a['text'], b['text'])

    tuites = [t for t in data if not match(REGEX_RETWEETED, t['text'])]
    print('Total tuites', len(tuites))

    similarity = []
    print('checking similatiry')

    for a, b in itertools.combinations(tuites, 2):
        similarity.append(check_similarity(a, b))

    duplicated_tweets = [(a, b) for a, b, ratio in similarity if ratio >= 0.7]

    save_to_html(duplicated_tweets, 'check-similarity')


def bot_by_name(data):

    all_screen_name = [
        d['user']['screen_name'] for d in data]

    bots = [
        s for s in all_screen_name if match(REGEX_BOT_BY_NAME, s)
    ]

    save_to_html(bots, 'bot-by-name')
