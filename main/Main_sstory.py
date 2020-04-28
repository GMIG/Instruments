import mpv
import logging

from mpv_simple import MpvSimple
from mpv_simple import LoopPlayer
from function_caller import FunctionCaller

from twisted.internet import reactor
from pynput import keyboard

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s.%(msecs)03d:\t%(message)s', datefmt='%I:%M:%S')

    logging.debug('logging')
    
    #mpv = MpvSimple('test')
    #pl = LoopPlayer('loop')
    #pl.names.append('drop.avi')
    #pl.names.append('bird.avi')
    #pl.names.append('sp.jpeg')
    #pl.start()
    
    sstory = MpvSimple('sstory')
    
    def fadeBackgroundAndPlay():
        sstory.fade(1)
        def playStory(x):
            sstory.play('story.avi')
        sstory.caller.on_faded(playStory)
        
    def goBackToBackground():
        sstory.play('background.jpeg')
        sstory.setSoundChannels(left=False,right=False)

    def fileEnded(filename):
        if filename=='background.jpeg':
            sstory.play('background.jpeg')
        if filename=='story.avi':
            goBackToBackground()
    sstory.caller.on_end_file(fileEnded)
        
    def leftEarUp():
        if not sstory.rightChannel:
            fadeBackgroundAndPlay()
            sstory.setSoundChannels(left=True,right=False)
        else:
            sstory.setSoundChannels(left=True,right=True)
    
    def leftEarDown():
        if not sstory.rightChannel:
            goBackToBackground()
        else:
            sstory.setSoundChannels(left=False,right=True)
            
    def rightEarUp():
        logging.debug(sstory.leftChannel)
        if not sstory.leftChannel:
            fadeBackgroundAndPlay()
            sstory.setSoundChannels(left=False,right=True)
        else:
            sstory.setSoundChannels(left=True,right=True)
    
    def rightEarDown():
        if not sstory.leftChannel:
            goBackToBackground()
        else:
            sstory.setSoundChannels(left=True,right=False)
    
    sstory.play('background.jpeg')
            
    fakeArduino = FunctionCaller("fa")
    fakeArduino.on_0(leftEarUp)
    fakeArduino.on_1(leftEarDown)
    fakeArduino.on_2(rightEarUp)
    fakeArduino.on_3(rightEarDown)

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

