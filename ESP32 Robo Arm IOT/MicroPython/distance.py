# This code is Distance sensor in Pico
# Red LED - Tank is full
# Green LED - Tank is empty
# Yellow LED - Tank Water level is medium

from machine import Pin
import utime

trigger = Pin(3, Pin.OUT)
echo = Pin(2, Pin.IN)
led = Pin(4, Pin.OUT)
led2 = Pin(5, Pin.OUT)
led3 = Pin(6, Pin.OUT)

def ultra():
  global signalon 
  global signaloff
  trigger.low()
  utime.sleep_us(2)
  trigger.high()
  utime.sleep_us(5)
  trigger.low()
  while echo.value()==0:
    signaloff = utime.ticks_us()
  while echo.value()==1:
    signalon = utime.ticks_us()
  timepassed = signalon - signaloff
  distance = (timepassed*0.0343)/2
  if distance<100:
    led.on()
  else:
    led.off()
  if distance>300:
    led2.on()
  else:
    led2.off()
  if 100<distance<400:
    led3.on()
  else:
    led3.off()

while True:
  ultra()

