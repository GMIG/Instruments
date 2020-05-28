from function_caller import FunctionCaller
from tcp_receiver import TCPReceiver
from tcp_client import TCPClient
from twisted.internet import reactor
import pytest

import logging

logging.basicConfig(level=logging.DEBUG,format='%(asctime)s.%(msecs)03d:\t%(message)s', datefmt='%I:%M:%S')

def prepare():
    host = FunctionCaller('host')
    factHost = TCPReceiver(2232)
    factHost.parts[host.name]=host

    client = FunctionCaller('client')
    factClient = TCPClient('127.0.0.1',2232)
    factClient.parts[client.name]=client
    
def test_sendClient():
    host = FunctionCaller('host')
    factHost = TCPReceiver(2232)
    factHost.parts[host.name]=host
    factHost.begin()
    def initClient():
        client = FunctionCaller('client')
        factClient = TCPClient('127.0.0.1',2232)
        factClient.parts[client.name]=client
        factClient.begin()
    reactor.callLater(3.5, initClient)
    reactor.run()

