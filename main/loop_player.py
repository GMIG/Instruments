from mpv_simple import MpvSimple
from function_caller import FunctionCaller

class LoopPlayer:
    def __init__(self, name:str):
        self.names = []
        self.splayer = MpvSimple(name+'.simplePlayer')
        self.caller=FunctionCaller(name)        
        self.splayer.caller.on_end_file(self.next)          

    def next(self,filename):
        ind = self.names.index(filename)
        if ind==len(self.names)-1:
            newInd=0
        else:
            newInd=ind+1
        self.splayer.player.loadfile(self.names[newInd])
        self.caller.runFunction('end_file',str(self.splayer.player.filename))
          
    def start(self,i:int = 0):
        self.splayer.player.loadfile(self.names[i])

