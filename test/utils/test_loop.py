#!/usr/bin/python

def run(system_data):
    for component_name, component_class, component_args in system_data:
        if component_args is not None:
            print component_name + "," + str(component_class) + "," +','.join(component_args)
        else:
            print component_name + "," + str(component_class)
            
if __name__ == '__main__':
    SYSTEM_DATA = (
        ('asus_computer', 22, ('asus', 'text1' )),
        ('intel_computer', 33, ('intel', )),
        ('intel', 44,None),
        ('amd', 55,None),
    )
    
    run(SYSTEM_DATA)