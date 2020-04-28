import mpv
import logging

from mpv_simple import MpvSimple
from mpv_simple import LoopPlayer
from function_caller import FunctionCaller
from tcp_receiver import TCPReceiver,TCPClient

from twisted.internet import reactor
from pynput import keyboard
import sys 


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s.%(msecs)03d:\t%(message)s', datefmt='%I:%M:%S')

    logging.debug('logging')
    
    #mpv = MpvSimple('test')
    #pl = LoopPlayer('loop')
    #pl.names.append('drop.avi')
    #pl.names.append('bird.avi')
    #pl.names.append('sp.jpeg')
    #pl.start()
    logging.debug(sys.argv[1])
    vid = LoopPlayer('vid')
    vid.names.append('drop.avi')
    vid.start()
    
    if sys.argv[1] == 'host':
        main = FunctionCaller('host')
        fact = TCPReceiver(8007)
        fact.parts[main.name]=main
        fact.begin()
        def sendSync():
            fact.sendAll('cl.sync()')
        vid.caller.on_end_file(sendSync)
    if sys.argv[1] == 'cl':
        cl = FunctionCaller('cl')
        def restartPlayer():
            vid.start()
        cl.on_sync(restartPlayer)
        fact = TCPClient('127.0.0.1',8007)
        fact.parts[cl.name]=cl
        fact.begin()



    def on_press(key):
        logging.debug(key)
        if key.char == 'k':
            sstory.setFadeTime(1,finish=1)
        if key.char == 'l':
            sstory.setFadeTime(1)
        if key.char in ['0','1','2','3']:
            fakeArduino.runFunction(str(key.char))
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

    
    #pl.splayer.loopCall.start(0.05)
    reactor.run()

