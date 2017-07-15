# -*- coding: utf-8 -*-
from  bottle import route,run,static_file
'''
@route('https://sam-for-test-leon-ghibli-1.c9users.io')
def home():
    return 

@route('/')
def main():
    return static_file('index.html',root='.')
run(host='locahost',port='9999')
'''

@route('https://sam-for-test-leon-ghibli-1.c9users.io/echo/<thing>')
def echo(thing):
    return 'Say hello to Sam: %s! '%thing
run(host='localhost',port='8080')