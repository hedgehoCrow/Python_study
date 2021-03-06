#!/usr/bin/env python3
# coding: UTF-8

import gevent
from gevent_zeromq import zmq

context = zmq.Context()

def server():
    server_socket = context.socket(zmq.REQ)
    server_socket.bind("tcp://127.0.0.1:5000")

    for request in range(1, 10):
        server_socket.send("Hello")
        print ('Switched to Sever for ', request)

        server_socket.recv()

def client():
    client_socket = context.socket(zmq.REP)
    client_socket.connect("tcp://127.0.0.1:5000")

    for request in range(1, 10):
        client_socket.recv()
        print ('Switched to Client for ', request)

        client_socket.send("World")

publisher = gevent.spawn(server)
client    = gevent.spawn(client)

gevent.joinall([publisher, client])

