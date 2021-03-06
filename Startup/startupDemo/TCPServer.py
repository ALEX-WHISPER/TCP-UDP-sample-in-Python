# coding=gbk
'''
Created on 2018��10��17��
@author: �����
'''

from socket import *
from threading import Thread

def main():
    # create welcome socket for all requesting clients
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind(('', serverPort))
    
    # accepted clients dictionary
    dic = {}
    
    # listen to clients for 'knocking to the welcome door'
    serverSocket.listen(2)
    print('The server is ready to receive...')
    
    try:
        while True:
            # create connectionSocket for the single client after accepting
            connectionSocket, addr = serverSocket.accept()
            if (not(dic.__contains__(addr))):
                dic[addr] = connectionSocket
        
                p = Thread(target = msgToUpper, args = (connectionSocket, addr))
                p.start()
    finally:
        serverSocket.close()

def msgToUpper(connectionSocket, addr):
    while True:
        msgFrmC = connectionSocket.recv(1024).decode()
        if (len(msgFrmC) > 0):
            modifiedMessage = msgFrmC.upper()
            print("Msg from client(%s:%s): %s" % (addr[0], addr[1], msgFrmC))
            print('Response: ' + modifiedMessage)
            connectionSocket.send(modifiedMessage.encode())
        else:
            break
    connectionSocket.close()
        

if __name__=="__main__":
    main()