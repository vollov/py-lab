# -*- coding: utf-8 -*-

import sqlite3

class SqlMem:
    
    def __init__(self):
        self.connection = sqlite3.connect('../../etc/updates.db')
        
    def initTables(self):
        cursor = self.connection.cursor()
        cursor.execute('''CREATE TABLE stocks
             (date text, trans text, symbol text, qty real, price real)''')
        self.connection.commit()
        self.connection.close()
        
    def saveStatus(self):
        print 'OK'