from setuptools import find_packages, setup

from utils import __version__

setup(
    name='suricate',
    url='https://github.com/rougeth/rabisco/',
    version=__version__,
    author='Johni Douglas Marangon',
    author_email='johni.douglas.marangon@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tweepy',
        'pymongo',
        'python-dotenv',
        'click',
        'jinja2',
    ],
    entry_points={
        'console_scripts': 'suricate=cli:cli'
    },
)
