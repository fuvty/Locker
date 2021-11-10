import cv2
import face_recognition
import time
from entrance_guard.utils import my_face_recognition
from entrance_guard.FaceRec import RecInterface
from outer_io.keypad import Keypad
from outer_io.motor import Motor
from outer_io.light import Light
from enum import Enum

from events import lock_toggle

class Controller:
    class State(Enum):  # 状态
        WAITING = 0
        RECOGNITION = 1
        ENTER_PASSWORD = 2
        CHANGE_PASSWORD = 3
        SAVE_IMAGE = 4
        DEBUG = -1

    def __init__(self):
        '''
        init outer_io
        '''
        self.light = Light(3)
        self.motor = Motor([19,26], [6,13])
        self.keypad = Keypad()

        self.status = self.State.DEBUG
        # keychain = KeyChain()
        while(True):
            time.sleep(1)
            self.decision()

    def decision(self):
        if self.status == self.State.WAITING:
            '''
            init state, wait for keyboard
            '''
            # raise NotImplementedError
            key = self.keypad.getKey()
            if key == 'A':
                print('A')
                self.status = self.State.RECOGNITION
            elif key == 'D':
                print('D')
                self.status = self.State.DEBUG
            else:
                raise NotImplementedError
        elif self.status == self.State.RECOGNITION:
            '''
            rec and get auth
            '''
            auth = RecInterface()
            if auth:
                lock_toggle.lock_open(self.motor, self.light)
            else:
                self.status = self.State.WAITING   
        elif self.status == self.State.ENTER_PASSWORD:
            '''
            enter password and unlock
            '''
            # auth = PasswordInterface()
        elif self.status == self.State.CHANGE_PASSWORD:
            '''
            change password
            ''' 
            # keyChain.change()
            self.status = self.State.WAITING
        elif self.status == self.State.SAVE_IMAGE:
            '''
            write face info
            '''
            
            self.status = self.State.WAITING
        elif self.status == self.State.DEBUG:
            '''
            debug purpose
            '''
            lock_toggle.lock_open(self.motor, self.light)
            # self.light.blink(loop_time= 3)
            # self.motor.pull()
            # light.blink(loop_time= 3)
            # motor.push()
            self.status = self.State.WAITING
            

if __name__ == '__main__':
    Controller()
