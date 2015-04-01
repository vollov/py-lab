class InvalidFileError(Exception): pass

class Filehandler:
    
    def __init__(self, file_path):
        self._file_path = file_path
        
    def read(self):
        with open(self._file_path, 'r') as file_handler:
            lines = file_handler.readlines()
            lines = filter(None, (line.strip() for line in lines))
            print lines
            
def run():
    t1 = [12,23,45]
    message= 'sddd {}  xxx {}'.format(len(t1),33)
    print message
    
    file_path = 'c:\\test\\aaax.psf'
    handler = Filehandler(file_path)
    try:
        handler.read()
    except IOError as e:
        print 'Erorr when reading file ' + file_path + ' ' + str(e)
        
if __name__=='__main__':run()
        