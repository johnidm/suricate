The propouse of this project is to have fun.

suricate is a simple tool to collect data on Twitter to analyse and classify social bots accounts

Suricate (in Brazilian Portuguese) is a small species of foraging mammal that is found inhabiting the harsh conditions of the open and arid, semi-desert plains in southern Africa, [see more](https://a-z-animals.com/animals/meerkat/).

### Usage

```
$ pip install --editable .
$ suricate --helps
```

### Understanding the Configurations

The configurations setting is defined on the `config.py` file.

### Setup MongoDB with Docker 

```
docker volume create mongodbdata
docker run -d -p 27017:27017 -v mongodbdata:/data/db mongo
```