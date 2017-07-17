# -*- coding: utf-8 -*-
# for subscribe 
import zmq
host = '127.0.0.1'
port = 6789
ctx = zmq.Context()
sub = ctx.socket(zmq.SUB)
sub.connect('tcp://%s:%s')%(host,port)
topics = ['maine coon','persian']
for topic in topics:
    sub.setsockopt(zmq.SUBSCRIBE,topic.encode('utf-8'))
while True:
    cat_bytes,hat_bytes = sub.recv_multipart()
    print 'sub.recv_multipart()', sub.recv_multipart()
    cat = cat_bytes.decode('utf-8')
    hat = hat_bytes.encode('utf-8')
    print 'Subscibe: %s wears a %s' %(cat,hat)
    