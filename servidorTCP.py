# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula  (python 3)
#

# importacao das bibliotecas
from socket import * # sockets

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 62000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))
while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  if sentence == 'obter arquivo.txt':
    arquivo = open('arquivo.txt', 'r', encoding='utf-8').read()
    print ('Cliente %s enviou: %s, resposta gerada: %s' % (addr, sentence, arquivo))
    connectionSocket.send(arquivo.encode('utf-8')) #envia ao cliente o texto do arquivo
  else:
    erro = 'comando inválido'
    print ('Cliente %s enviou: %s, resposta gerada: %s' % (addr, sentence, erro))
    connectionSocket.send(erro.encode('utf-8')) #envia ao cliente o texto do arquivo
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor