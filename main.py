import cv2
import face_recognition
import time
from entrance_guard.utils import my_face_recognition
from entrance_guard.FaceRec import RecInterface
from outer_io.motor import Motor

def main():
    status = 11
    motor = Motor([19,26], [6,13])
    # keychain = KeyChain()
    while(True):
        time.sleep(0.1)
        if status == 0:
            '''
            init state, wait for keyboard
            '''
            raise NotImplementedError
            # key = getKey()
            # if key == "A":
                # status = 1
        elif status == 1:
            '''
            rec and get auth
            '''
            auth = RecInterface()
            if auth:
                status = 10
            else:
                status = 0   
        elif status == 2:
            '''
            enter password and unlock
            '''
            # auth = PasswordInterface()
        elif status == 3:
            '''
            change password
            ''' 
            # keyChain.change()
            status = 0
        elif status == 10:
            '''
            open the door 
            '''
            motor.pull()
        elif status == 11:
            '''
            close the door 
            '''
            motor.push()
        elif status == -1:
            '''
            debug purpose
            '''
            continue

if __name__ == '__main__':
    main()
