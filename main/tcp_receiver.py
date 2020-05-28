
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory,ClientFactory
from twisted.internet.endpoints import TCP4ServerEndpoint
from function_caller import FunctionCaller
from tcp_protocol import TCPProtocol
from twisted.internet import reactor

import typing
import logging



class TCPReceiver(Factory):
    def __init__(self, port):
        super().__init__()
        self.parts:typing.Dict[str,FunctionCaller] = dict()
        self.receivers = set()
        self.__port = port

    def begin(self):
        self.endpoint = TCP4ServerEndpoint(reactor, self.__port)
        self.endpoint.listen(self)
        
    def startFactory(self):
        pass

    def stopFactory(self):
        pass
        
    def sendAll(self,message:str):
        for recv in self.receivers:
            for part in self.parts.keys():
                recv.send(part,message)
    
    def buildProtocol(self, addr):
        observer = TCPProtocol(self)
        return observer
        

