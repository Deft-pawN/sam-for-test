# -*- coding: utf-8 -*-
import redis 
import random
conn = redis.Redis()
# topic is cats ,message is hat
cats = ['siamese','persian','maine coon','norwegin forest']
hats = ['stovepipe','bowler','tam-o-shanter','fedora']
for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print ("Publish :%s wears a %s")%(cat,hat)
    conn.publish(cat,hat)