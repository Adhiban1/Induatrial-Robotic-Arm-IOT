# **************************************#
# Author: George Bantique               #
#         TechToTinker Youtube Channel  #
#         TechToTinker.blogspot.com     #
#         tech.to.tinker@gmail.com      #
# Date: Nov.13, 2020                    #
# Please feel free to modify the code   #
# according to your needs.              #
# **************************************#


# **************************************
# Load necessary libraries
import machine
import network 
import urequests 
import time
import esp32

ssid = b"Heisenberg's WiFi"
password = "%q$jJeGIK#GgLlg#"
# **************************************
# Create objects:
led = machine.Pin(2,machine.Pin.OUT) 



# **************************************
# Configure the ESP32 wifi as STAtion
sta = network.WLAN(network.STA_IF)
if not sta.isconnected(): 
  print('connecting to network...') 
  sta.active(True) 
  #sta.connect('your wifi ssid', 'your wifi password') 
  sta.connect(ssid, password) 
  while not sta.isconnected(): 
    pass 
print('network config:', sta.ifconfig()) 


# **************************************
# Constants and variables:
HTTP_HEADERS = {'Content-Type': 'application/json'} 
THINGSPEAK_WRITE_API_KEY = 'S9M9SSMJP5XXZE21' 
UPDATE_TIME_INTERVAL = 5000  # in ms 
last_update = time.ticks_ms() 
# initially there would be some delays 
# before submitting the first update 
# but should be enough to stabilize the 
# the DHT sensor. 


# **************************************
# Main loop:
while True: 
    if time.ticks_ms() - last_update >= UPDATE_TIME_INTERVAL: 
        tf = esp32.raw_temperature()
        tc = (tf-32)/1.8
        t_readings = {'field1':tf, 'field2':tc} 
        request = urequests.post( 
          'http://api.thingspeak.com/update?api_key=' +
          THINGSPEAK_WRITE_API_KEY, 
          json = t_readings, 
          headers = HTTP_HEADERS )  
        request.close() 
        print(t_readings) 
         
        led.value(not led.value()) 
        last_update = time.ticks_ms()