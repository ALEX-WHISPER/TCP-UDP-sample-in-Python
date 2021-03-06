# coding=gbk
'''
Created on 2018年10月17日
@author: 钟以琛
'''

from socket import *
from pip._vendor.distlib.compat import raw_input

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM);
message = raw_input('Input message:') # raw_input(): python 内置 api

'''
等待接受来自 server 的数据
数据将被赋给 modifiedMessage, 源地址将被赋给 serverAddress (ip + port)
buffer length: 2048
'''
while message != 'EOF':
    # encode(): string->byte
    # sendto(): 向  clientSocket 发送结果分组(源地址将自动附上)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    message = raw_input('Input message:')

print('Close socket')
clientSocket.close()
