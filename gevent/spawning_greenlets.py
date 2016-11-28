#!/usr/bin/env python3
# coding: UTF-8

import gevent
from gevent import Greenlet

def foo(message, n):
    gevent.sleep(n)
    print (message)

if __name__ == '__main__':
    thread1 = Greenlet.spawn(foo, "Hello", 1)
    thread2 = gevent.spawn(foo, "I live!", 2)
    thread3 = gevent.spawn(lambda x: (x+1), 2)

    threads = [thread1, thread2, thread3]

    gevent.joinall(threads)

