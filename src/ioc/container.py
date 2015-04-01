#!/usr/bin/python
import types,json,os,sys
from pc.computer import Computer,IntelCpu,AMDCpu

#import types
##import pc.computer
#from pc.computer import Computer,IntelCpu,AMDCpu
#
#class Container:
#    def __init__(self, system_data):
#        for component_name, component_class, component_args in system_data:
#            if type(component_class) == types.ClassType:
#                if component_args is not None:
#                    args = [self.__dict__[arg] for arg in component_args]
#                    self.__dict__[component_name] = component_class(*args)
#            else:
#                self.__dict__[component_name] = component_class
# 
#if __name__ == '__main__':
#    SYSTEM_DATA = (
#        ('asus_computer', Computer, ('asus', )),
#        ('intel_computer', Computer, ('intel', )),
#        ('intel', IntelCpu,None),
#        ('amd', AMDCpu,None),
#    )
#    c = Container(SYSTEM_DATA)
#    intel = c.intel_computer.setCpu(c.intel)
#    
#    print c.intel_computer.getCpu()



class Container:
    '''IOC Container read the json file to load the objects and store them into 
    dictionary'''
    
    
    def __init__(self, conf_file_path):
        self.conf_file_path = conf_file_path
        self.parseConfig()
        
    def parseConfig(self):
        conf_file_handler = open(self.conf_file_path, 'r')
        content = conf_file_handler.read()
        conf_file_handler.close()
        #print content
        data = json.loads(content)
        for k, v in data.iteritems():
            for item in v:
                self.initComponent(item)
#            print item['id'] + ":" + item['clazz']

            
    def initComponent(self, json_item):
        ''' Initialize current component defined in by json_item '''
        
        print 'initComponent() --> Initialize class ' + json_item['clazz']
        component_class = json_item['clazz']
        parameter_list = []
        for i in json_item['parameters']:
            if i['type'] == 'number' or i['type'] == 'string':
                parameter_list.append(i['value'])
            else:
                parameter_list.append(self.__dict__[i['value']])
        self.__dict__[json_item['id']] = component_class(*parameter_list)
        
#        if type(component_class) == types.ClassType:
#            print component_class
#            for i in item['parameters']:
#                print 'type-->'+i['type']    
#        else:
            
            
#            self.__dict__[json_item['id']] = component_class()
    
    def getSelf(self):
        return self.__dict__;
         
def import_class(cl):
    d = cl.rfind(".")
    classname = cl[d+1:len(cl)]
    m = __import__(cl[0:d], globals(), locals(), [classname])
    return getattr(m, classname)
   
def test():
    current_directory = os.path.dirname(os.path.abspath(__file__))
    base_directory = os.path.join(current_directory, '..')
    conf_dir = os.path.join(base_directory, 'etc')
    json_path = os.path.join(conf_dir, 'computer.json')
#    c = Container(json_path)
#    print c.getSelf()

###################################
# method 1
###################################
#    dict={}
#    clazz_list=[IntelCpu,AMDCpu]
#    for c in clazz_list:
#        dict[c] = c(3.6)
#        
#    print dict
###################################
# method 2
###################################
    xx = IntelCpu()
    xx.setSpeed(3.6)
    print xx.getSpeed()
    
    dict={}
    clazz_list=['pc.computer.IntelCpu','pc.computer.AMDCpu']
    for c in clazz_list:
        x=import_class(c)
        #x.setSpeed(3.6)
        dict[c] = x

    print dict
    
if __name__ == '__main__':test()