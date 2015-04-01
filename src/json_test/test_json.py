#!/usr/bin/python

import json, unittest

"""Test json method
dumps(object) -- translate obj to a JSON formatted str
loads(str) -- translate a JSON str a Python object
"""
class Project:
    def __init__(self, oid=None, name=None):
        self.id = oid
        self.name = name
    
    def dict(self):
        return {'id':self.id, 'name':self.name}
    
    def __repr__(self):
        return "<Project('%d', '%s')>" % (self.id, self.name)
    
    @staticmethod
    def decode(dict):
        return Project(dict['id'], dict['name'])

class TestJSON(unittest.TestCase):
    
    def test_loads_complex(self):
        project = json.loads('''{"id":2,"name":"project 1dd"}''', object_hook=Project.decode)
        print 'loads object:',project
        
    def test_dumps(self):
        product_list = [
        {
            "id": 0,
            "title": "Paint pots",
            "description": "Pots full of paint",
            "price": 3.95
        },
        {
            "id": 1,
            "title": "Polka dots",
            "description": "Dots with that polka groove",
            "price": 12.95
        },
        {
            "id": 2,
            "title": "Pebbles",
            "description": "Just little rocks, really",
            "price": 6.95
        }]
        result = json.dumps(product_list)
        print 'dumps:',type(result), result
        
    def test_loads(self):
        json_text = '''[
        {
            "id": 0,
            "title": "Paint pots",
            "description": "Pots full of paint",
            "price": 3.95
        },
        {
            "id": 1,
            "title": "Polka dots",
            "description": "Dots with that polka groove",
            "price": 12.95
        },
        {
            "id": 2,
            "title": "Pebbles",
            "description": "Just little rocks, really",
            "price": 6.95
        }]'''
        result = json.loads(json_text)
        print 'load:',type(result), result