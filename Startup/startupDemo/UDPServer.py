# coding=gbk
'''
Created on 2018��10��17��
@author: �����
'''

from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive...')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    if (len(message) > 0):
        print('msg from client: ' + message.decode())
        print('msg to client: ' + modifiedMessage)
    serverSocket.sendto(modifiedMessage.encode(), clientAddress)
