from flask_pymongo import PyMongo
import config
from application import app
# Database Connection


def database_connection():
    app.config['MONGO_URI'] = 'mongodb://{username}:{password}@{host_name}:{port}/{database}'.format(
        username=config.MONGODB_USERNAME,
        password=config.MONGODB_PASSWORD,
        host_name=config.MONGODB_HOST,
        port=config.MONGODB_PORT,
        database=config.MONGODB_NAME)
    app.config['MONGO_CONNECT'] = False
    mongo = PyMongo(app)
    return mongo