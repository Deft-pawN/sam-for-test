# -*- coding: utf-8 -*-
import threading
print threading.__file__
import os 
import time 
import redis
import multiprocessing
def dryer():
    conn = redis.Redis()
    pid = os.getpid()
    timeout = 20
    print "Dryer process %s is staring " %(pid)
    while True:
        msg = conn.blpop('dishes',timeout)#dishes is a queue 
        if not msg:
            break
        val = msg[1].decode('utf-8')
        if val =="quit":
            break
        print ('%s:dried %s')%(pid,val)
        time.sleep(0.1)
    print("Dryer process %s is done")%(pid)# 20s returns none and finished the process


for i in range(3):
    p = multiprocessing.Process(target=dryer)
    p.start()



    