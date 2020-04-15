from GitHelp import GitHelp
from Pipeline import Pipeline

class CommandDev:

    def __init__(self,):
        pass
    
    def process(self,):
        
        pipeline = Pipeline()
        pipeline.loadFile('./proton.yml')
        self.fluxo =  pipeline.getJson()


        for services in self.fluxo['path']:
            self.processService(services)

       
        #git = GitHelp()
        #git.clone('https://bitbucket.org/corebiz_ag/admin_animale.git',"aa/c/s")

    def processService(self, service_name):
        service = self.fluxo['path'][service_name]

        user = self.fluxo['auth']['user']
        token = self.fluxo['auth']['token']
        git = GitHelp(user,token)


        git.clone(service['git'], '.', service_name)
        #process sub
        print('process sub .....')
        for sub in service['sub']:
            subservice = service['sub'][sub]
            git.clone(subservice['git'], service_name + '/'+subservice['src'])
            
       


        