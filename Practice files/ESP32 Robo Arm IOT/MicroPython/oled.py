# ssd1306 128x64 OLED display with I2C interface

from machine import Pin, I2C
from utime import sleep
from ssd1306 import SSD1306_I2C

sda = Pin(20)
scl = Pin(21)

i2c = I2C(0, sda=sda, scl=scl, freq=400000)


oled = SSD1306_I2C(128, 32, i2c)

oled.text('Hello', 0, 0)
oled.text('Pi Pico', 0, 10)
oled.text('OLED Display', 0, 20)
oled.show()
sleep(4)

oled.fill(1)
oled.show()
sleep(2)
oled.fill(0)
oled.show()

while True:
    oled.text('Hello World', 0, 0)
    for i in range(164):
        oled.scroll(1, 0)
        oled.show()
        sleep(0.01)
