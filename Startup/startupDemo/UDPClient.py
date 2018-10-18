# coding=gbk
'''
Created on 2018��10��17��
@author: �����
'''

from socket import *
from pip._vendor.distlib.compat import raw_input

serverName = '127.0.0.1'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_DGRAM);
message = raw_input('Input message:') # raw_input(): python ���� api

'''
�ȴ��������� server ������
���ݽ������� modifiedMessage, Դ��ַ�������� serverAddress (ip + port)
buffer length: 2048
'''
while message != 'EOF':
    # encode(): string->byte
    # sendto(): ��  clientSocket ���ͽ������(Դ��ַ���Զ�����)
    clientSocket.sendto(message.encode(), (serverName, serverPort))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    print(modifiedMessage.decode())
    message = raw_input('Input message:')

print('Close socket')
clientSocket.close()