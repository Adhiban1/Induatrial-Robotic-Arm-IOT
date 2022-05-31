import serial.tools.list_ports
import serial
from time import sleep

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for oneport in ports:
    portList.append(str(oneport))

print(portList)

val = input("Select the port: COM")

for x in portList:
    if x.startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(x)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()


def angles(a):
    if 0 < len(a) <= 3:
        a = f"{int(a):3.0f}".replace(" ", "0").replace("  ", "00")
        print(a)
        for i in a:
            serialInst.write(str(i).encode("utf-8"))
            sleep(0.1)


while True:
    angles(input("Angle: "))
