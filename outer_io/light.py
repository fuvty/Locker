import time
from gpiozero import LED

class Light:
    def __init__(self, pin: int) -> None:
        self.led = LED(3)
    def on(self):
        self.led.on()
    def off(self):
        self.led.off()
    def blink(self, loop_time= 5):
        for i in range(loop_time):
            self.led.toggle()
            time.sleep(0.5)
            self.led.toggle()
            time.sleep(0.5)