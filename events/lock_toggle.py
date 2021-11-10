from outer_io.motor import Motor
from outer_io.light import Light

def lock_open(motor: Motor, light: Light):
    motor.pull(max_time=0)
    light.blink(loop_time= 3)
    motor.stop()

def lock_close(motor: Motor, light: Light):
    motor.push(max_time=0)
    light.blink(loop_time= 3)
    motor.stop()