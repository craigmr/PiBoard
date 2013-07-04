'''
Created on Sep 26, 2012

@author: csimpson
'''
import subprocess
import time

class BreadBoard:
    doorActive = False
    
    @staticmethod
    def readPin(pin):
        process = subprocess.Popen(['gpio', 'read', str(pin)], stdout=subprocess.PIPE)
        state, _ = process.communicate()
        state = str.replace(state, "\r", "")
        state = str.replace(state, "\n", "")
        return int(state)

    @staticmethod
    def setPin(pin, value):
        subprocess.call(['gpio', 'mode',str(pin), 'out'])
        subprocess.call(['gpio', 'write', str(pin), str(value)])
    
    @staticmethod    
    def isGarageOpen():
        if BreadBoard.readPin(0) == 1:
            return True
        else:
            return False
        
    @staticmethod
    def activateGarageDoor():
        if not BreadBoard.doorActive:
            BreadBoard.doorActive = True
            BreadBoard.setPin(7, 1)
            time.sleep(2)
            BreadBoard.setPin(7, 0)
            BreadBoard.doorActive = False
            
    @staticmethod
    def notifiyBuild(passed):
        if passed:
            print 'Set green'
            BreadBoard.setPin(1,1)
            BreadBoard.setPin(0,0)
        else:
            print 'Set red'
            BreadBoard.setPin(1,0)
            BreadBoard.setPin(0,1)
            
    @staticmethod
    def turnOffNotify():
        BreadBoard.setPin(0,0)
        BreadBoard.setPin(1,0)    
        
        
