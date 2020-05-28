from twisted.internet.protocol import Factory,ClientFactory
from function_caller import FunctionCaller
from twisted.internet import reactor
from tcp_protocol import TCPProtocol


class TCPClient(ClientFactory):
    def __init__(self, host, port):
        super().__init__()
        self.parts:typing.Dict[str,FunctionCaller] = dict()
        self.receivers = set()
        self.__host = host
        self.__port = port
    def begin(self):
        self.endpoint = reactor.connectTCP(self.__host, self.__port, self)
        
    def sendAll(self,message:str):
        for recv in self.receivers:
            for part in self.parts.keys():
                recv.send(part,message)

    def buildProtocol(self, addr):
        return TCPProtocol(self)
