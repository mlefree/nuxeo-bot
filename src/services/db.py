import os

from pymongo import MongoClient


class ServicesBD:
    """
        MongoDB decorator used by Services
    """

    def __init__(self, active=False):
        if active:
            MONGO_URL = os.environ.get('MONGO_URL', 'mongodb://localhost:27654')
            print('MONGO_URL:' + MONGO_URL)
            self.mongo = MongoClient(MONGO_URL)
            self.db = self.mongo.db

        pass

    def getDB(self):
        return self.db
