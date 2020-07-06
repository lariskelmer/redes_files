# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Base de um servidor HTTP (python 3)
#

# importacao das bibliotecas
import socket
import os, string, codecs
# definicao do host e da porta do servidor
HOST = '' # ip do servidor (em branco)
PORT = 8080 # porta do servidor

# cria o socket com IPv4 (AF_INET) usando TCP (SOCK_STREAM)
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# permite que seja possivel reusar o endereco e porta do servidor caso seja encerrado incorretamente
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# vincula o socket com a porta (faz o "bind" do IP do servidor com a porta)
listen_socket.bind((HOST, PORT))

# "escuta" pedidos na porta do socket do servidor
listen_socket.listen(1)

# imprime que o servidor esta pronto para receber conexoes
print ('Serving HTTP on port %s ...' % PORT)

while True:
    # aguarda por novas conexoes
    client_connection, client_address = listen_socket.accept()
    print(client_connection, client_address)

    
    while True:

        # o metodo .recv recebe os dados enviados por um cliente atraves do socket
        request = client_connection.recv(1024)
        print(request.decode('utf-8'))
        # imprime na tela o que o cliente enviou ao servidor

        split_file = (request.decode('utf-8')).split()
        request = split_file
        
        if split_file[0] == 'end':
            client_connection.close()
            break
        
        elif split_file[0] == 'GET':
            # suportando entradas "GET /path HTTP/1.1" ou "GET / HTTP/1.1" ou "GET /HTTP/1.1";
            # I:   split_file[0] = 'GET'; split_file[1] = '/path'; split_file[2] = 'HTTP/1.1';
            # II:  split_file[0] = 'GET'; split_file[1] = '/'; split_file[2] = 'HTTP/1.1;
            # III: split_file[0] = 'GET'; split_file[1] = '/HTTP/1.1';

            path = split_file[1]
            
            # 'GET' sem maiores especificações, envia index.html:

            if path == '/' or path == '/HTTP/1.1' or path == '':

                print('request: '+str(request))

                client_connection.send('HTTP/1.0 200 OK\n'.encode("utf-8"))
                client_connection.send('Content-Type: text/html\n'.encode("utf-8"))
                client_connection.send('\n'.encode("utf-8"))
                f = codecs.open('index.html', 'r')
                http_response = f.read()
                client_connection.send(http_response.encode('utf-8'))

            # 'GET' pedindo algum arquivo:
            else:
                #path = path.split('/')
                # supondo o formato: /path/index.html, path[0] = /path,
                #path[1] = index.html
                try:
                    f = codecs.open('.'+path, 'r')
                    http_response = f.read()
                    client_connection.send(http_response.encode('utf-8'))
                    # servidor retorna o que foi solicitado pelo cliente (neste caso a resposta e generica)
                    pass
                
                except:    
                    #path = path.split('/')
                    for i in range(0, len(path)):
                        fav_ico = path.split('.')
                   
                        if fav_ico[i] == '.ico':
                            client_connection.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode("utf-8"))
                            print('HTTP/1.1 404 Not Found\r\n\r\n')

                        else:
                            client_connection.send('HTTP/1.1 404 Not Found\r\n\r\n'.encode("utf-8"))
                            f = codecs.open('index_error.html', 'r')
                            http_response = f.read()
                            client_connection.send(http_response.encode('utf-8'))                   
                    pass
        else:
            client_connection.send('HTTP/1.1 400 Bad Request\r\n\r\n'.encode("utf-8"))
            f = codecs.open('index_erro_2.html', 'r')
            http_response = f.read()
            print(http_response)
            client_connection.send(http_response.encode('utf-8'))
            break
        break
    client_connection.close()
listen_socket.close()
