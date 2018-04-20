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

Realiza a coleta de dados
```
suricate collect --tag="" --keywords=""
```

#### Report

Extrai dados de uma coleção e salva em arquivos CSV
```
suricate report --tag="" --model=""
```

Relatórios disponíveis
- screen-name
- text-not-retweeted
- text-retweeted
- text

#### Rules
Executar regras de extração de dados e gera um arquivo HTML
```
suricate rule --tag="" --name=""
```

Regras disponíveis (name):
- check-similarity
- bot-by-name