from setuptools import setup, find_packages

setup(
    name='suricate',
    url='https://github.com/rougeth/rabisco/',
    version='0.1',
    author='Johni Douglas Marangon',
    author_email='johni.douglas.marangon@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'tweepy',
        'pymongo',
        'python-dotenv',
        'click',
    ],
    entry_points={
        'console_scripts': 'suricate=cli:cli'
    },
)