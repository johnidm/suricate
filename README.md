The propouse of this project is to have fun.

Suricate (in Brazilian Portuguese) is a small species of foraging mammal that is found inhabiting the harsh conditions of the open and arid, semi-desert plains in southern Africa, [see more](https://a-z-animals.com/animals/meerkat/).

### Understanding the Configurations

The configurations setting is defined on the `config.py` file.

- MONGO_DB_URL: Database address to connect to a MongoDB instance, [see more](https://docs.mongodb.com/manual/reference/connection-string/).




mkdir data
docker run -d -p 27017:27107 -v data:/data/db mongo