# -*- coding: utf-8 -*-
#利用 redis 生成一个队列
import redis 
conn = redis.Redis()
print "Washing is staring "
dishes = ['salad','bread','entree','dessert']
for dish in  dishes:
    msg = dish.encode('utf-8')
    conn.rpush('dishes',msg)
    print ('Washed',dish)
conn.rpush('dishes','quit')
print 'Washer is done '