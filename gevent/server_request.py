# coding: UTF-8

#import gevent.moneky
#gevent.monkey.patch_socket()

import gevent
import urllib.request
import simplejson as json

def fetch(pid):
    # http://json-time.appspot.com/time.json is 404
    response = urllib.request.urlopen('http://json-time.appspot.com/time.json')
    result = response.read()
    json_result = json.loads(result)
    datetime = json_result['datetime']
    
    print ('Process ', pid, datetime)
    return json_result['datetime']

def synchronous():
    for i in range(1, 10):
        fetch(i)

def asynchronous():
    threads = []
    for i in range(1, 10):
        threads.append(gevent.spawn(fetch, i))
    gevent.joinall(threads)

print ('Synchronous:')
synchronous()

print ('Asynchronous:')
asynchronous()

