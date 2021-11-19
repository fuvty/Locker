# This program allows a user to enter a
# Code. If the C-Button is pressed on the
# keypad, the input is reset. If the user
# hits the A-Button, the input is checked.

import RPi.GPIO as GPIO
import time

class Keypad:
    def __init__(self) -> None:
        
        # These are the GPIO pin numbers where the lines and columns
        # of the keypad matrix are connected
        self.L1 = 7   
        self.L2 = 8   
        self.L3 = 25   
        self.L4 = 24   
        self.C1 = 12
        self.C2 = 16
        self.C3 = 20
        self.C4 = 21

        # The GPIO pin of the column of the key that is currently
        # being held down or -1 if no key is pressed
        self.keypadPressed = -1
        self.secretCode = "3333"
        self.input = ""
        self.key=""
        self.quit=False
        self.check=False

        # Setup GPIO
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(self.L1, GPIO.OUT)
        GPIO.setup(self.L2, GPIO.OUT)
        GPIO.setup(self.L3, GPIO.OUT)
        GPIO.setup(self.L4, GPIO.OUT)

        # Use the internal pull-down resistors
        GPIO.setup(self.C1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.C4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

        # This callback registers the key that was pressed
        # if no other key is currently pressed
        def keypadCallback(channel):
            if self.keypadPressed == -1:
                self.keypadPressed = channel

        # Detect the rising edges on the column lines of the
        # keypad. This way, we can detect if the user presses
        # a button when we send a pulse.
        GPIO.add_event_detect(self.C1, GPIO.RISING, callback=keypadCallback)
        GPIO.add_event_detect(self.C2, GPIO.RISING, callback=keypadCallback)
        GPIO.add_event_detect(self.C3, GPIO.RISING, callback=keypadCallback)
        GPIO.add_event_detect(self.C4, GPIO.RISING, callback=keypadCallback)


    # Sets all lines to a specific state. This is a helper
    # for detecting when the user releases a button
    def setAllLines(self,state):
        GPIO.output(self.L1, state)
        GPIO.output(self.L2, state)
        GPIO.output(self.L3, state)
        GPIO.output(self.L4, state)

    def input_password(self):
        while not self.quit:
        # If a button was previously pressed,
        # check, whether the user has released it yet
            if self.keypadPressed != -1:
                self.setAllLines(GPIO.HIGH)
                if GPIO.input(self.keypadPressed) == 0:
                    self.keypadPressed = -1
                else:
                    time.sleep(0.1)
            # Otherwise, just read the input
            else:
                key=self.getKey()
                if key=='*':
                    if self.input == self.secretCode:
                        print("Code correct!")
                        self.quit=True
                        self.check=True
                        # TODO: Unlock a door, turn a light on, etc.
                    else:
                        print("Incorrect code!")
                        # TODO: Sound an alarm, send an email, etc.
                        self.input=""
                elif key=='#':
                    print("Input reset!")
                    self.input=""
                elif key=='D':
                    self.quit=True
                    self.input=""
                else:
                    self.input+=key
                    print("当前key:",key)
                    print("当前input",self.input)       
                time.sleep(0.1)

    def change_password(self):
        new_password=""
        while not self.quit:
        # If a button was previously pressed,
        # check, whether the user has released it yet
            if self.keypadPressed != -1:
                self.setAllLines(GPIO.HIGH)
                if GPIO.input(self.keypadPressed) == 0:
                    self.keypadPressed = -1
                else:
                    time.sleep(0.1)
            # Otherwise, just read the input
            else:
                key=self.getKey()
                if key=='*':
                    if(len(new_password)<1):
                        print("New password shouldn't be NULL")
                        new_password=""
                    else:
                        print("New password has been set!")
                        self.secretcode=new_password
                elif key=='#':
                    print("Input reset!")
                    new_password=""
                elif key=='D':
                    self.quit=True
                    new_password=""
                else:
                    new_password+=key
                    print("当前key:",key)
                    print("当前password",new_password)       
                time.sleep(0.1)
            


    # def checkSpecialKeys(self):
        
    #     pressed = False

    #     ## 检查是否确认密码  *
    #     GPIO.output(self.L4, GPIO.HIGH)
    #     if (not pressed and GPIO.input(self.C1) == 1):
    #         if self.input == self.secretCode:
    #             print("Code correct!")
    #             self.quit=True
    #             self.check=True
    #             # TODO: Unlock a door, turn a light on, etc.
    #         else:
    #             print("Incorrect code!")
    #             # TODO: Sound an alarm, send an email, etc.
    #         self.input=""
    #         pressed = True
    #     GPIO.output(self.L4, GPIO.LOW)


    #     ## 检查是否输入重置  #
    #     GPIO.output(self.L4, GPIO.HIGH)
    #     if (GPIO.input(self.C3) == 1):
    #         print("Input reset!")
    #         pressed = True
    #         self.input=""
    #     GPIO.output(self.L4, GPIO.LOW)

    #     return pressed


    # reads the columns and appends the value, that corresponds
    # to the button, to a variable
    def readLine(self, line, characters):
        # We have to send a pulse on each line to
        # detect button presses
        
        key=""
        GPIO.output(line, GPIO.HIGH)
        if(GPIO.input(self.C1) == 1):
            key=characters[0]
        if(GPIO.input(self.C2) == 1):
            key=characters[1]
        if(GPIO.input(self.C3) == 1):
            key=characters[2]
        if(GPIO.input(self.C4) == 1):
            key=characters[3]
        GPIO.output(line, GPIO.LOW)

        return key

    def getKey(self):
        while True:
            # If a button was previously pressed,
            # check, whether the user has released it yet
            if self.keypadPressed != -1:
                self.setAllLines(GPIO.HIGH)
                if GPIO.input(self.keypadPressed) == 0:
                    self.keypadPressed = -1
                else:
                    time.sleep(0.1)
            # Otherwise, just read the input
            else:            
                key1=self.readLine(self.L1, ["1","2","3","A"])
                key2=self.readLine(self.L2, ["4","5","6","B"])
                key3=self.readLine(self.L3, ["7","8","9","C"])
                key4=self.readLine(self.L4, ["*","0","#","D"])
                self.key=key1+key2+key3+key4
                if self.key != "":
                    return self.key
                time.sleep(0.1)

if __name__=="__main__":
    keypad = Keypad()
    while True:
        key=keypad.getKey()
        print(key)

        