import pymongo

import config


class MongoManager:

    def __init__(self):
        self.mongo_user = 'root'
        self.mongo_pwd = 'example'
        self.mongo_host = config.mongo_host
        self.myclient = pymongo.MongoClient(f"mongodb://{self.mongo_user}:{self.mongo_pwd}@{self.mongo_host}:27017/")

    def insert_data(self, db_name, collection_name, data):
        mydb = self.myclient[db_name]
        mycol = mydb[collection_name]
        mycol.insert_many(data)
