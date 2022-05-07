import keyboard
import serial.tools.list_ports
import serial
from time import sleep
import sys
import colorama
from colorama import Fore
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

colorama.init(autoreset=True)
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []

for oneport in ports:
    portList.append(str(oneport))

print(portList)
print(Fore.CYAN + "Select the port: COM", end="")
val = input()

for x in portList:
    if x.startswith("COM" + str(val)):
        portVar = "COM" + str(val)
        print(Fore.RED + x)

serialInst.baudrate = 9600
serialInst.port = portVar
serialInst.open()


def send(i):
    serialInst.write(str(i).encode("utf-8"))


while True:
    try:
        # os.system("cls")
        print(serialInst.readline().decode().rstrip())
        # os.system("cls")
    except:
        pass
    if keyboard.is_pressed("esc"):
        sys.exit()
    if keyboard.is_pressed("a"):
        send("a")
    if keyboard.is_pressed("s"):
        send("s")
    if keyboard.is_pressed("d"):
        send("d")
    if keyboard.is_pressed("f"):
        send("f")
    if keyboard.is_pressed("g"):
        send("g")
    if keyboard.is_pressed("h"):
        send("h")
    if keyboard.is_pressed("x"):
        send("x")
        print(Fore.GREEN + "Automation...")
        engine.say("Automation")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed("q"):
        send("q")
        print(Fore.GREEN + "Cleared...")
        engine.say("Cleared")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed("y"):
        send("y")
        print(Fore.GREEN + "Default position...")
        engine.say("Default position")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed("r"):
        send("r")
        print(Fore.GREEN + "Recorded...")
        engine.say("Recorded")
        engine.runAndWait()
        # sleep(1)
