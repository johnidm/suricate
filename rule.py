import itertools
from difflib import SequenceMatcher

from utils import REGEX_BOT_BY_NAME, REGEX_RETWEETED, match, save_to_html, flat_list


def apply(data, name):

    RULES = {
        'check-similarity': check_similarity,
        'bot-by-name': bot_by_name,
        'tweet-urls': tweet_url,
    }

    RULES[name](data)


def tweet_url(data):
    urls_raw = list(filter(None, [d['entities']['urls'] for d in data]))

    urls = [d['expanded_url'] for d in flat_list(urls_raw)]

    save_to_html(urls, 'tweet-urls')


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
