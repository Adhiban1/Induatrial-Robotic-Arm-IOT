# This program for Servo Motor
# YouTube Link: https://www.youtube.com/watch?v=6qdrGwonmrM

from machine import Pin, PWM
from time import sleep_ms

MIN_DUTY = 1000
MAX_DUTY = 9000

pwm = PWM(Pin(15))
pwm.freq(50)

duty = MIN_DUTY
direction = 1

while True:
    for _ in range(1024):
        duty += direction
        if duty > MAX_DUTY:
            duty = MAX_DUTY
            direction = -direction
        
        elif duty < MIN_DUTY:
            duty = MIN_DUTY
            direction = -direction
        
        pwm.duty_u16(duty)
