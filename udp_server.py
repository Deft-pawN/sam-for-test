# -*- coding: utf-8 -*-
from datetime import datetime
import socket

server_address = ('locahost',6789)
max_size = 4096

print 'Staring the server at',datetime.now()
print 'Waiting for a client to call '
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind(server_address)
data,client = server.recvfrom(max_size)
print ('AT',datetime.now(),client,'said',data)
server.sendto(b'Are you talking to me?',client)
server.close()


