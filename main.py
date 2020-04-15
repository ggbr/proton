#!/usr/bin/env python3
from os import system
from time import sleep
import sys
from CommandDev import CommandDev
# Derruba o Serviço Stack do Muffato
#system('docker stack down admin')

command = sys.argv[1]


if (command == "pro"):
    print('copiando arquivos ...')
    system('cp auto/docker-compose-deploy.yml docker-compose.yml')
    system('cp auto/Makefilepro Makefile')
    system('cp app/.env.example .env')


elif (command == "dev"):
    print('copiando arquivos ...')
    system('cp auto/docker-compose.yml docker-compose.yml')
    system('cp auto/Makefiledev Makefile')



elif (command == "build"):
    v = sys.argv[2]
    system('docker login')

    system('docker build  ./app -t corebiz/api-admin:' + v)
    system('docker push corebiz/api-admin:' + v)

elif(command == "clone"):
    #print("clonando ...")
    #git = GitHelp()
    #git.clone('https://bitbucket.org/corebiz_ag/admin_animale.git',"aa/c/s")
    commandDev = CommandDev()
    commandDev.process()

    
else:
    print('Comando não encontrado')
