#!/usr/bin/env python3
# coding: UTF-8

from gevent import sleep
from gevent.pool import Pool
from gevent.coros import BoundedSemaphore

sem = BoundedSemaphore(2)
    
def worker1(n):
    sem.acquire()
    print ('Worker %i acquired semaphore' % n)
    sleep(0)
    sem.release()
    print ('Worker %i released semaphore' % n)

def worker2(n):
    with sem:
        print ('Worker %i acquired semaphore' % n)
        sleep(0)
    print ('Worker %i released semaphore' % n)


def main():
    pool = Pool()
    pool.map(worker1, range(0, 2))
    pool.map(worker2, range(3, 6))

if __name__ == '__main__':
    main()


