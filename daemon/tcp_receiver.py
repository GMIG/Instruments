
from twisted.protocols.basic import LineReceiver
from twisted.internet.protocol import Factory
from twisted.internet.endpoints import TCP4ServerEndpoint
from function_caller import FunctionCaller
from twisted.internet import reactor

import typing
import logging
import re


class TCPReceiverProtocol(LineReceiver):
    def __init__(self, factory ):
        LineReceiver.__init__(self)
        self.delimiter=b'\r'
        self.__factory=factory
        self.__parts=factory.parts
        #Observable.__init__(self, 'tcp')
        #self.setLineMode()
        #self.decoding_talker = compose(self.say_array, self.codec)
        #self.add_listener("cmd", self.process_result)
        self.__current_command_id: int = 3
        self.__issued_command_storage = {}
        self.__commandRE = re.compile('(\[(\S+)\])?([\S]+)\.(\S+)\((.*)\)')
        #self.delimiter = '\n'

    def connectionMade(self):
        # self.factory was set by the factory's default buildProtocol:
        self.__factory.receivers.add(self)
        logging.debug('connected')
        LineReceiver.connectionMade(self)
        
    def connectionLost(self, reason):
        self.__factory.receivers.discard(self)
        logging.debug('disconnected')
        LineReceiver.connectionLost(self, reason)
        
    def rawDataReceived(self, data):
        logging.debug( data)
        return

    def lineReceived(self, datab):
        logging.debug( datab)
        #return
        data = str(datab, 'ascii')
        logging.debug('received'+data)        
        try:
            matches = self.__commandRE.match(data)
            if matches == None:
                logging.debug('could not decode \'' + data + '\' - skipping')
                return
            decodedString = dict(code=matches.group(2),part=matches.group(3),command=matches.group(4),args=matches.group(5))
            logging.debug('received and decoded ' + str(decodedString))

            if decodedString['part'] not in self.__parts:
                logging.debug('part \'' + decodedString['part'] + '\' not found - skipping')
                return
        except ValueError as err:
            logging.debug('could not decode \'' + data + '\' - skipping')
            return
        else:
            result = (self.__parts[decodedString['part']].runFunction(decodedString['command'],decodedString['args']))
            if result is not None:
                self.send(decodedString['part'],result) 
            return
        
    def send(self, part, message):
        self.sendLine(bytes(str(part)+ ':' + str(message), 'ascii')) 

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
        observer = TCPReceiverProtocol(self)
        return observer
