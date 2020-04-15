import yaml
import json

class Pipeline:

    def __init__(self,):
        self.pipeline = None
    
    def loadFile(self, src):
        with open(r'' + src) as file:
            fruits_list = yaml.load(file, Loader=yaml.FullLoader)
            self.pipeline = fruits_list
    
    def getJson(self,):
        return self.pipeline