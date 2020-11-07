#!/usr/bin/python3
# -*- coding: utf-8 -*-

__author__       = 'Gabriel Gregório da Silva'
__email__        = 'gabriel.gregorio.1@outlook.com'
__description__  = 'Analisa diversos IPS no LINUX (UBUNTU) e mostra quais estão respondendo.'
__status__       = 'Development'
__date__         = '14/09/2019'
__last_update__  = '21/09/2019'
__version__      = '0.2'

from os import system
import os
from os import remove
from threading import Thread
from time import sleep

global ips
ips = 0

global threads
threads = 0

def loc(ip):
    global ips
    global threads
    threads += 1

    try:
        cmd = "ping -c4 " + ip
        resposta = "".join(os.popen(cmd).readlines())

        if 'ttl=' in resposta:
            print('Ip encontrado: ', ip)
            ips += 1
    except Exception as erro:
        print("Erro no programa: ", erro)
    threads -= 1

print()
print("********************************************")
print("* Como funciona?")
print("* Você digita uma classe de Ip, exemplo: ")
print("* 192.168.0")
print("*")
print("* O programa irá executar centenas de pings")
print("* de 192.168.0.1 até 192.168.0.255")
print("* retornando quais computadores responderam")
print("*")
print("* Você pode digitar qual classe quiser, exemplos: ")
print("* 192.168.2")
print("* 192.168.100")
print("* 10.0.0")
print("********************************************")
print()

defina_ip = str(input('Digite uma classe de ip : '))

_min = 1
_max = 255
print("\nIniciando testes entre {} e {}".format(defina_ip+'.'+str(_min), defina_ip+'.'+str(_max)))
print("Finalização em {} s\n".format(0.3*255+8))
for x in range(_min, _max):
    ip = defina_ip + '.' + str(x)

    h = Thread(target=lambda ip=ip: loc(ip))
    h.start()
    sleep(0.3)

sleep(4)

while threads != 0:
    continue

if ips == 0:
    print("\nNenhum ip encontrado entre {} e {}".format(defina_ip+'.'+str(_min), defina_ip+'.'+str(_max)))


input('\n\nPressione enter para fechar')

