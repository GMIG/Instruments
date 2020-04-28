#PIPENV_VENV_IN_PROJECT
import logging
import typing
from twisted.internet import reactor
from function_caller import FunctionCaller
from tcp_receiver import TCPReceiver
import os
import psutil
 
if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('logging')
 
    def checkProcess():
        for proc in psutil.process_iter():
            logging.debug(proc.name()+' ' +str(proc.pid) +' '+ str(os.getpid()))
            if proc.name() == 'python' and proc.pid!=os.getpid() and proc.status()!=psutil.STATUS_ZOMBIE:
                return 'is_on'
        return 'is_off'
    def closeProcess():
        for proc in psutil.process_iter():
            if proc.name() == 'python' and proc.pid!=os.getpid():
                try:
                    proc.kill()
                except OSError as err:
                    return 'err'
        return 'ok'
    def runProcess():
        os.popen('sh /home/pi/autorun.sh')
        return 'ok'
    def osRestart():
        #os.system("sudo reboot")
        return
    def delayedSend(x):
        def f(x):
            fact.sendAll("somevent")
        reactor.callLater(3.5, f, "hello, world")
 
 
    dem = FunctionCaller("dem")
    dem.on_init(checkProcess)
    dem.on_check(checkProcess)
    dem.on_switch_off(closeProcess)
    dem.on_switch_on(runProcess)
    dem.on_restart(osRestart)
    dem.on_ds(delayedSend)
 
    fact = TCPReceiver(8007)
    fact.parts[dem.name]=dem
    fact.begin()
 
    reactor.run()
