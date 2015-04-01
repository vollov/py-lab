#!/usr/bin/python

import json

def test():
    fin = open('computer.json', 'r')
    content = fin.read()
    fin.close()
    #print content
    data = json.loads(content)
    #print data
    #json.decoder()
    
    for key, va in data.iteritems():
        print 'key->',key        
        for item in va:
            print item['id'] + ":" + item['clazz']
            for i in item['parameters']:
                print 'type-->'+i['type']
            

if __name__ == '__main__':test()    
