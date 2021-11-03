from typing import List
from gpiozero import LED
import RPi.GPIO as GPIO
import time

class Motor:
    def __init__(self, pin_push: List[int], pin_pull: List[int]) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(pin_push[0], GPIO.OUT)
        GPIO.setup(pin_push[1], GPIO.OUT)
        GPIO.setup(pin_pull[0], GPIO.OUT)
        GPIO.setup(pin_pull[1], GPIO.OUT)
        self.pin_push = pin_push
        self.pin_pull = pin_pull

    def push(self, max_time =3):
        GPIO.output(self.pin_push[0], GPIO.HIGH)
        GPIO.output(self.pin_push[1], GPIO.HIGH)
        GPIO.output(self.pin_pull[0], GPIO.LOW)
        GPIO.output(self.pin_pull[1], GPIO.LOW)
        time.sleep(max_time)
        GPIO.output(self.pin_push[0], GPIO.LOW)
        GPIO.output(self.pin_push[1], GPIO.LOW)
        GPIO.output(self.pin_pull[0], GPIO.LOW)
        GPIO.output(self.pin_pull[1], GPIO.LOW)

    def pull(self, max_time =3):
        GPIO.output(self.pin_push[0], GPIO.LOW)
        GPIO.output(self.pin_push[1], GPIO.LOW)
        GPIO.output(self.pin_pull[0], GPIO.HIGH)
        GPIO.output(self.pin_pull[1], GPIO.HIGH)
        time.sleep(max_time)
        GPIO.output(self.pin_push[0], GPIO.LOW)
        GPIO.output(self.pin_push[1], GPIO.LOW)
        GPIO.output(self.pin_pull[0], GPIO.LOW)
        GPIO.output(self.pin_pull[1], GPIO.LOW)

    

if __name__ == "__main__":
    moter = Motor([19,26], [6,13])
    moter.push(5)
    moter.pull(5)

