#!/usr/bin/python
import unittest, sqlalchemy
from sqlalchemy.engine import create_engine
from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import Column, Integer, String

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    password = Column(String(50))
    
    def __init__(self, name, password):
        self.name = name
        self.password = password
        
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

class UserUt(unittest.TestCase):
    '''A Unit Test Demo'''

#    def setUp(self):


    def test_int(self):
        engine = create_engine('mysql://root:justdoit@localhost/issue_pool', echo=True)
        engine.execute("select 1").scalar()
        print sqlalchemy.__version__ 
        Base.metadata.create_all(engine) 
#        self.assertEquals(2,2,'number not equals')
        
#    def test_vehicle(self):
#        v = Vehicle('Corolla')
#        v.display()

if __name__=='__main__': unittest.main()