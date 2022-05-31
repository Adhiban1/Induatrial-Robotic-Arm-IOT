import serial
from serial.tools import list_ports

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for oneport in ports:
    portList.append(str(oneport))

print(portList)
print("Select the port: COM", end="")
val = input()

for x in portList:
    if x.startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(x)

with open("port.txt", "w") as f:
    f.write(portVar)
