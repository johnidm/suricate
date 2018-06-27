The propose of this project is to have fun.

Suricate is a simple tool to collect data on Twitter to analyse and classify social bots accounts

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

### Development environment 

I am using Jupyter Notebook to test the code. 

```
pip install jupyter
```
```
jupyter notebook
```

### Avaliable commands

#### Collect

Collects data and saves to a Mongo collection

```
suricate collect --tag="" --keywords=""
```

#### Report

Extract data and save to CSV file.

```
suricate report --tag="" --model=""
```

Avaliable reports:

- screen-name
- text-not-retweeted
- text-retweeted
- text

#### Rules

Run the rules to extract data. Save in the HTML file.

```
suricate rule --tag="" --name=""
```

Avaliable rules:

- check-similarity
- bot-by-name
