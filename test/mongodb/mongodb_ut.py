# -*- coding: utf-8 -*-

import unittest,os
from common import TestConfig
from configuration import Configuration
from mongodb import MongoDBConfig, MongoDB

class MongoDBUT(unittest.TestCase):
    def setUp(self):
        test_config = TestConfig()
        self.data_path = test_config.get_data_path()
        config = Configuration(os.path.join(self.data_path,'build.ini'))
        db_name = config.get('mongodb1','db_name')
        host = config.get('mongodb1','host')
        config = MongoDBConfig(db_name, host)
        self.db = MongoDB(config)
        
    def testInsert(self):
        hobby = ['AA','BB','CC']
        p1 = People('dustin',34,hobby)
        object_id = self.db.insert(p1.__dict__, 'people')
#        print object_id
        people = self.db.findOne({"_id":object_id},'people')
#        print people
        self.assertEquals(34, people['_age'], 'age should be 34')
        self.assertEquals(['AA','BB','CC'], people['_hobby'], '_hobby should be AA,BB,CC')
        
    def tearDown(self):
        "Delete seed data from testing database"
        self.db.removeAll('people')
        
class User:
    '''demo class for an OO design'''
    
    def __init__(self, name, passwd):
        self.name = name
        self.passwd = passwd

    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"
   
    def display(self):
        print "user name : ", self.name, self.passwd
        
class People:
    def __init__(self,name,age,hobby):
        self._name = name
        self._age = age
        self._hobby = hobby

    def setAddress(self,address):
        self._address = address
        
    def hobby(self):
        return self._hobby

class Address:
    def __init__(self,city, state):
        self._city = city
        self._state = state
    
def test():
    'planner'
    hobby = ['AA','BB','CC']
    p1 = People('dustin',34,hobby)
#    address = Address('waterloo', 'ON')
#    p1.setAddress(address)
    print p1.__dict__
    db = MongoDB()

if __name__ == '__main__':
    unittest.main()
#    test()