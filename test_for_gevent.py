# -*- coding: utf-8 -*-
import gevent
from gevent import socket
hosts = ['www.crappytaxidermy.com','wwww.walterpottertaxidermy.com','www.antique-taxidermy.com']
jobs = [gevent.spawn(gevent.socket.gethostbyname,host)for host in hosts]
gevent.joinall(jobs,timeout=5)
for job in jobs:
    print (job.value)