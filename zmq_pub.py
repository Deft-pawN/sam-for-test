# -*- coding: utf-8 -*-
import zmq
import random
import time
host = '*'
port = 6789
ctx = zmq.Context()
pub = ctx.socket(zmq.SUB)
pub.bind('tcp://%s:%s')%(ctx,port)
cats = ['siamese','persian','maine coon ','norwegin forest']
hats = ['stovepipe','bowler','tam-shanter','fedora']
time.sleep()
for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    cat_bytes = cat.encode('utf-8')
    hat_bytes = hat.encode('utf-8')
    print ('Publish :%s wears a %s')%(cat,hat)
    pub.send_multipart([cat_bytes,hat_bytes])