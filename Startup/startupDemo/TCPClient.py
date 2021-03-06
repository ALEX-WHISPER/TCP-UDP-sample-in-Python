# coding=gbk
'''
Created on 2018��10��17��
@author: �����
'''

from socket import *
from pip._vendor.distlib.compat import raw_input

# define destination address(ip + port)
serverName = '127.0.0.1'
serverPort = 12000

# create clientSocket
clientSocket = socket(AF_INET, SOCK_STREAM)

# connect to server to create a new TCP connection
clientSocket.connect((serverName, serverPort))

# input message, then throw it to the TCP connection
message = raw_input('Input message: ')

while message != 'EOF':
    clientSocket.send(message.encode())
    modifiedMessage = clientSocket.recv(1024)
    print('From server: ', modifiedMessage.decode())
    message = raw_input('Input message: ')

print('Close socket')
clientSocket.close()
