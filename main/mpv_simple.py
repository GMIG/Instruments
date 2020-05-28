import mpv
import logging
from function_caller import FunctionCaller
from twisted.internet import task
from twisted.internet import reactor
class MpvSimple:

    def __init__(self, name:str):
        logging.basicConfig(level=logging.DEBUG)
        logging.debug('logging')
        
        self.player = mpv.MPV(log_handler=print)
        self.player.set_loglevel('fatal')
    
        self.player.ontop=True
        self.player.volume=100
        self.player.image_display_duration=10
        self.player.border=False
        self.player.keep_open=True
        self.player.keep_open_pause=False
        self.player.screen=0
        self.player.geometry='500x500+700+500'
        self.fadingDelta=0
        self.fadingF=0.05
        self.rightChannel=True
        self.leftChannel=True

        #player.fullscreen=True
        #player.fs_screen=0
        self.caller=FunctionCaller(name)        
        @self.player.property_observer('eof-reached')
        def eof_reached(name,state):
            if state==True:
                self.caller.runFunction('end_file',str(self.player.filename))
        
        #Happens right before a new file is loaded. When you receive this, the player is loading the file (or possibly already done with it).
        @self.player.event_callback('start-file')
        def start_file(name):
            self.caller.runFunction('start_file',str(self.player.filename))
        
        def fade():
            try:
                prop = self.player._get_property('vf')
                brightness = float(prop[0]['params']['romax'])
                logging.debug("fade " + str(brightness))
                if self.fadingDelta != 0:
                    newBrightness=brightness+self.fadingDelta
                    if newBrightness >= 1.0:
                        self.fadingDelta=0
                        newBrightness=1.0
                        self.setBrightness(newBrightness)
                        self.caller.runFunction('unfaded',str(self.player.filename))
                    elif newBrightness <= 0:
                        self.fadingDelta=0
                        newBrightness=0#
                        self.setBrightness(newBrightness)
                        self.caller.runFunction('faded',str(self.player.filename))
                    else:
                        self.setBrightness(newBrightness)
            except Exception as e:
                logging.debug('Fade returned exception \'' + str(e) + '\'')
        self.setBrightness(1)
        self.loopCall = task.LoopingCall(fade)
        
    def setBrightness(self,x:int):
        self.player._set_property("vf",'colorlevels=romax='+str(x)+':gomax='+str(x)+':bomax='+str(x))

    def fade(self,time:int,finish:int = 0):
        prop = self.player._get_property('vf')
        brightness = float(prop[0]['params']['romax'])
        self.fadingDelta=(finish-brightness)/time*self.fadingF
        if not self.loopCall.running:
            reactor.callFromThread(self.loopCall.start,self.fadingF)

    def setSoundChannels(self,left:bool,right:bool):
        initStr=''
        if left:initStr+='|c0=c0'
        if right:initStr+='|c1=c1'
        self.leftChannel=left
        self.rightChannel=right
        logging.debug('Sound channels: left=' + str(self.leftChannel) + ',right='+str(self.rightChannel))
        self.player._set_property("af", "lavfi=[pan='stereo"+left+right+"']") 

        
    def play(self,filename:str):
        #logging.debug('Player ' + self.caller.name + ' begins playing file ' + filename)
        self.setBrightness(1)
        self.fadingDelta=0
        self.player.loadfile(filename)


        # @player.property_observer('time-pos')
        # def time_observer(_name, value):
            # caller.runFunction('time-pos')
            
        # @player.property_observer('filename')
        # def filename_observer(_name, value):
            # print('Filename ' + value)    
            
        # #Current position on playlist. The first entry is on position 0. Writing to this property may start playback at the new position.
        # @self.player.property_observer('playlist-pos')
        # def playlist(_name, value):
            # print(self)
            # self.caller.runFunction('playlist-pos',self.player.playlist_pos)   
                    
        #Happens after a file was unloaded. Typically, the player will load the next file right away, or quit if this was the last file.
        # @self.player.event_callback('end-file')
        # def end_observer(event):
            # self.caller.runFunction('end_file',str(event),str(self.player.filename),self.player._get_property("playlist-pos"))
            
        # #Start of playback after seek or after file was loaded
        # @self.player.event_callback('playback-restart')
        # def st_observer(name):
            # self.caller.runFunction('playback_restart',str(self.player.filename),self.player._get_property("playlist-pos"))
        
        # @self.player.property_observer('playlist-pos')
        # def my_handler(arg,arg2):
            # logging.debug("playlist-pos property " + str(arg) + ' ' + str(arg2))
            # self.caller.runFunction('playlist_pos',str(self.player.filename),self.player._get_property("playlist-pos"))

        # @self.player.event_callback('file-loaded')
        # def my_handler1(arg):
            # self.caller.runFunction('file_loaded',str(self.player.filename))
        
        #prop = mpv.player._get_property('vf')


            # print("file-loaded " + str(name))    
            
        #Start of playback after seek or after file was loaded.
        # @player.event_callback('playback-restart')
        # def ps_observer(name):
            # #if player.loop_file == 'inf':
            # #    changed(dict(code='playback-restart',oldFile=str(player.filename),newFile=str(player.filename))
            # logging.debug('playback-restart triggered')
            # logging.debug('filename:' + str(player.filename))
            # logging.debug('position in playlist:' + str(player.playlist_pos))
            
        #print(player.audio_device_list)
        #print(player.brightness)# = (-100)
        #player.contrast=100
        #print(player.brightness)# = (-100)
        #self.loadfile
        #player.command("vf","add","fade=type=out:start_time=1:duration=1")
        #player.command("vf","clr","")
        #player.command("vf","clr","")
        #this triggers only playback-restart
        #self.player.loop_file = 'inf'

        #player._set_property("vf",'eq=brightness=-0.5')
        #player.vf_add("fade=type=in:start_time=2:duration=1")
        #player.playlist_pos=1
        
        # DEBUG:root:function test.playback_restart added
        # DEBUG:root:playing 0
        # DEBUG:root:playlist-pos property playlist-pos 0
        # DEBUG:root:function test.playlist_pos not found - skipping
        # DEBUG:root:function test.start_file not found - skipping
        # DEBUG:root:running function test.playback_restart args 'sp.jpeg', 0

        # DEBUG:root:function test.end_file not found - skipping
        # DEBUG:root:function test.start_file not found - skipping
        # DEBUG:root:playlist-pos property playlist-pos 1
        # DEBUG:root:function test.playlist_pos not found - skipping
        # DEBUG:root:running function test.playback_restart args 'drop.avi', 1
        
        # DEBUG:root:function test.end_file not found - skipping
        # DEBUG:root:function test.start_file not found - skipping
        # DEBUG:root:playlist-pos property playlist-pos 2
        # DEBUG:root:function test.playlist_pos not found - skipping
        # DEBUG:root:running function test.playback_restart args 'bird.avi', 2
        
        #SINGLE FILE IN PLAYLIST
        # 05:32:36.625: playlist-pos property playlist-pos 0
        # 05:32:36.625: function test.playlist_pos not found - skipping
        # 05:32:37.245: function test.file_loaded not found - skipping
        # 05:32:37.477: function test.playback_restart not found - skipping
        # 05:32:43.543: running function test.end_file args "{'event_id': 7, 'error': 0, 'reply_userdata': 0, 'event': {'reason': 0, 'error': 0}}", 'drop.avi', 0
        # 05:32:43.543: function test.start_file not found - skipping
        # 05:32:43.576: function test.file_loaded not found - skipping
        # 05:32:43.618: function test.playback_restart not found - skipping
        
        #SINGLE FILE WITH RECALL
        # 05:37:49.354: playlist-pos property playlist-pos 0
        # 05:37:49.355: function test.playlist_pos not found - skipping
        # 05:37:49.356: function test.start_file not found - skipping
        # 05:37:49.727: function test.file_loaded not found - skipping
        # 05:37:49.947: function test.playback_restart not found - skipping
        # 05:37:56.013: running function test.end_file args "{'event_id': 7, 'error': 0, 'reply_userdata': 0, 'event': {'reason': 0, 'error': 0}}", 'drop.avi', 0
        # 05:37:56.014: function test.start_file not found - skipping
        # 05:37:56.015: running function test.end_file args "{'event_id': 7, 'error': 0, 'reply_userdata': 0, 'event': {'reason': 2, 'error': 0}}", 'bird.avi', 0
        # 05:37:56.015: function test.start_file not found - skipping
        # 05:37:56.016: running function test.end_file args "{'event_id': 7, 'error': 0, 'reply_userdata': 0, 'event': {'reason': 2, 'error': 0}}", 'bird.avi', 0
        # 05:37:56.016: function test.start_file not found - skipping
                    
