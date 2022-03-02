from machine import *
from time import sleep
i = 1
adc = ADC(Pin(33, Pin.IN))
while True:
    if adc.read_u16():
        print(f"{i} : Done")
        i += 1
    sleep(0.1)