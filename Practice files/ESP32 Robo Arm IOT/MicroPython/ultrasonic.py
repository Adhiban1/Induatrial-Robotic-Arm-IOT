import machine
import utime


def UltraSonic(Trig, Echo):  # Read ultrasonic function
    global pulse_start
    global pulse_end
    Trig.value(0)                       
    utime.sleep_us(2)
    Trig.value(1)
    utime.sleep_us(10)
    Trig.value(0)
    
    while Echo.value() == 0:
        pulse_start = utime.ticks_us()
        
    while Echo.value() == 1:
        pulse_end = utime.ticks_us()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration//58

    return distance

if __name__ == '__main__':

    # read ultrasonic

    Trig = machine.Pin(6,machine.Pin.OUT)   # Connect Trig pin to pin 6 and set to OUTPUT
    Echo = machine.Pin(8,machine.Pin.IN)    # Connect Echo pin to pin 7 and set to INPUT

    while True:
        print(UltraSonic(Trig, Echo))     # print ultrasonic distance
        utime.sleep(1)               # sleep 1 second
