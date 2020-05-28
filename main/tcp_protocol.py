
from twisted.protocols.basic import LineReceiver
import typing
import logging
import re
from function_caller import FunctionCaller

class TCPProtocol(LineReceiver):
    def __init__(self, factory ):
        LineReceiver.__init__(self)
        self.__factory=factory
        self.__parts=factory.parts
        self.setLineMode()
        self.__current_command_id: int = 3
        self.__issued_command_storage = {}
        self.__commandRE = re.compile('(\[(\S+)\])?([\S]+)\.(\S+)\((.*)\)')
        self.delimiter = b'\r'
        self.__parts['sys'] = FunctionCaller('sys')

    def connectionMade(self):
        self.__factory.receivers.add(self)
        self.__parts['sys'].runFunction('connected',self.transport.getPeer().host)        
        LineReceiver.connectionMade(self)
        
    def connectionLost(self, reason):
        self.__factory.receivers.discard(self)
        LineReceiver.connectionLost(self, reason)
        
    def rawDataReceived(self, data):
        logging.debug( data)
        return

    def lineReceived(self, datab):
        logging.debug( datab)
        data = str(datab, 'ascii')
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
        self.sendLine(bytes(str(message), 'ascii'))
