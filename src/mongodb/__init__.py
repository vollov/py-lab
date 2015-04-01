# -*- coding: utf-8 -*-
import sys,pymongo

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.code import Code

class MongoDBConfig:
    def __init__(self, db_name, host):
        self._db_name= db_name
        self._host = host

class MongoDB:
    '''Use mongo_client for a pooled mongodb'''

    def __init__(self, config):
        self.db_name = config._db_name
        try:
            self.connection = pymongo.MongoClient(host=config._host,auto_start_request=False)
        except ConnectionFailure, e:
            sys.stderr.write("Could not connect to MongoDB: %s" % e)
            sys.exit(1)

    def insert(self, doc, collection_name):
        'insert a document into a collection'
            
        db_handler = self.connection[self.db_name]
        assert db_handler.connection == self.connection
        with self.connection.start_request():
            object_id = db_handler[collection_name].insert(doc, safe=True)
        return object_id
    
    def findOne(self, query, collection_name):
        db_handler = self.connection[self.db_name]
        assert db_handler.connection == self.connection
        with self.connection.start_request():
            result = db_handler[collection_name].find_one(query)
        return result
        
    def removeAll(self, collection_name):
        db_handler = self.connection[self.db_name]
        assert db_handler.connection == self.connection
        with self.connection.start_request():
            db_handler[collection_name].remove()
        
