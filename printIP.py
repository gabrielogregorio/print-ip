#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__       = 'Gabriel Gregório da Silva'
__email__        = 'gabriel.gregorio.1@outlook.com'
__description__  = 'Analisa diversos IPS no LINUX (UBUNTU) e mostra quais estão respondendo.'
__status__       = 'Development'
__date__         = '14/09/2019'
__last_update__  = '15/09/2019'
__version__      = '0.1'

print('*********** carregando software ********')

from os import system
from os import remove
from threading import Thread

print('\n*********** biliotecas importadas ******')

global itens
global x
global andante
global defina_ip

itens = []
andante = 0

def loc():
    global x
    global andante
    global defina_ip

    andante += 1
    try:
        ip = defina_ip + str(x)
        print('testando.: {}\r'.format(ip),end='')
        system('ping -c 2 {} > {}'.format(ip,ip))

        a = open(ip,'r')
        b = a.read()
        a.close()

        if 'ttl=' in b:
            global itens
            itens.append(ip)
        remove(ip)
    except:
        pass
    andante -= 1


# programa
defina_ip = str(input('Digite um ip alvo (192.168.0.) : '))
a         = str(input('Começar testar a partir de (0) : '))
b         = str(input('Testar até qual  ip (150)      : '))

print('\n*********** iniciando testes ***********')
for x in range(int(a),int(b)):
    h = Thread(target=loc)
    h.start()

print('\n*********** aguardando respostas *******')
while andante != 0:
    print('ips encontrados: ({}) | restantes: ({}) \r'.format(len(itens),andante),end='')
print('\n*********** respostas OK ***************')


print('\n*********** ips encontrados ************')
for g in itens:
    print(g)

input('\n*********** pressione enter ************')

