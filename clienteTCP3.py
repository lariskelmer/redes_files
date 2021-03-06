# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Cliente de sockets TCP modificado para enviar texto minusculo ao servidor e aguardar resposta em maiuscula (python 3)
#

# importacao das bibliotecas
from socket import *
import os
# definicao das variaveis
serverName = '192.168.0.19' # ip do servidor
serverPort = 62000 # porta a se conectar
clientSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
clientSocket.connect((serverName, serverPort)) # conecta o socket ao servidor

while 1:
    sentence = input('Digite o comando: ')
    clientSocket.send(sentence.encode('utf-8')) # envia o texto para o servidor
    resposta = clientSocket.recv(1024) # recebe do servidor a resposta

    if sentence == 'fim':
        print ('O servidor (\'%s\', %d) encerrou' % (serverName, serverPort))
        clientSocket.close() # encerramento o socket do cliente
        break

    else:
        print ('O servidor (\'%s\', %d) respondeu: %s' % (serverName, serverPort, resposta.decode('utf-8')))
        continue

    

