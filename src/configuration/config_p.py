import ConfigParser,ast,os

class configp():
    def __init__(self):
        current_directory = os.path.dirname(os.path.abspath(__file__))
        self._config_file_path = os.path.join(current_directory, 'conf.ini')
        self.config = ConfigParser.ConfigParser()
        self.config.read(self._config_file_path)
        
    def get(self, section,option):
        return self.config.get(section, option)
    
def test():
    con = configp()
    print con.get('My Section','foodir')
    
if __name__=='__main__':test()