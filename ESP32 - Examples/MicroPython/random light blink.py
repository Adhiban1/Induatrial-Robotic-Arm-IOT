from machine import *
from time import *
import random


pin = Pin(2, Pin.OUT)
pwm = PWM(pin)
while True:
    pwm.duty(100)
    sleep(random.random())
    pwm.duty(500)
    sleep(random.random())
    pwm.duty(1000)
    sleep(random.random())