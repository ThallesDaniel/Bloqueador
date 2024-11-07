from pymongo import MongoClient

class MongoDBConnection:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="blocker_db"):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]
    
    def get_collection(self, collection_name):
        return self.db[collection_name]
