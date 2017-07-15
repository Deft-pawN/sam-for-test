# -*- coding: utf-8 -*-
import redis
conn = redis.Redis()
topics = ['maine coon','persian']
sub = conn.pubsub()
sub.subscribe(topics)#subscrible
for msg in sub.listen():
#listen return with a dict 
    if msg['type'] =="message":
        cat =msg['channel']
        hat = msg['data']
        print 'Subsrible:%s wears a %s'%(cat,hat)