import config
import argparse

from commands import collect_twittes


def collect(collection_name, keywords):

    if not collection_name:
        raise argparse.ArgumentError(None, 'DB Collettion name is not defined. Please, use the parameter "-c" or "--collection_name" to set it.')

    if len(keywords) == 0:
        raise argparse.ArgumentError(None, 'Keywords to collect not defined. Please use the parameter "-k" or "--keywords" to set it.')

    collect_twittes(collection_name, keywords)


def rule(beta):
    print('rule')


def execute():

    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='commands')

    parser_collect = subparsers.add_parser('collect')    
    parser_collect.add_argument(
        '-c', '--collection_name', dest='collection_name', type=str, help='Name of database collection')
    parser_collect.add_argument(
        '-k', '--keywords', dest='keywords', default=[], nargs='+', type=str, help='Keywords to collect tweets')

    parser_rule = subparsers.add_parser('rule')
    # parser_b.add_argument(
    #     '-b', '--beta', dest='beta', help='Beta description')
    # parser_b.add_argument(
    #     '-g', '--gamma', dest='gamma', default=42, help='Gamma description')

    kwargs = vars(parser.parse_args())
    globals()[kwargs.pop('commands')](**kwargs)


if __name__ == '__main__':
    execute()    


