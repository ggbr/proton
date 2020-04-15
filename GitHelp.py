import subprocess
import git
from os import system
from os import environ
from getpass import getpass
import subprocess
class GitHelp:

    def __init__(self,user = None, token = None):
        self.version = "0.1"
        self.user = user
        self.token = token

    def urlAuth(self,url):
        auth = self.user + ':' + self.token +'@'
        url_auth = url[0:8] + auth + url[8:]
        return  url_auth

    def clone(self, url, local = ".", path_name = None):
        #git.Git(path).clone(url)
        url_auth = self.urlAuth(url)
        if (local == "."):
            git.Git(local).clone(url_auth, path_name)
        else:
            #cria pastas onde vai fazer o clone
            self.create_path(local)
            #faz o clone na pasta
            try:
                git.Git(local).clone(url_auth, path_name)
            except git.exc.GitError:
                print('NameError')

    #função para criar as pastas 
    def create_path(self,path):
        #pega a string do caminho e separa as pastas
        elements = path.split('/')

        # verificar se o primeiro argumento 
        # foi o diretorio atual
        if elements[0] == ".":
            pasta = ''
        else:
            pasta = '.'

        # cria uma pasta em cada nivel do diretorio
        for e in elements:
            pasta = pasta + '/'+ e
            print(pasta)
            try:
                subprocess.call(['mkdir',pasta])
            except OSError:
                print('ok')

        #git("clone", "https://bitbucket.org/corebiz_ag/microservices-admin.git")
