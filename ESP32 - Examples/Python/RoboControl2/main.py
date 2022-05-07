import keyboard
import serial.tools.list_ports
import serial
from time import sleep
import sys
import colorama
from colorama import Fore
import pyttsx3
import getpass

colorama.init(autoreset=True)

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

instructions = f"""{Fore.RED}Controls:
{Fore.YELLOW}
* X-Axis: d(+) & a(-)
* Y-Axis: w(+) & s(-)
* Z-Axis: r(+) & f(-)
* q - Record the position
* e - Automation
* z - Move
* x - Default Position
* c - Clear Data
* esc - Close the App
"""
print(instructions)
i = 0
print(f"{Fore.GREEN}[Enter the password, you have only three Chances]")
engine.say("Enter the password, you have only three Chances")
engine.runAndWait()
while True:
    print(f"{Fore.MAGENTA}")
    password = getpass.getpass()
    if password == "eie":
        print(f"{Fore.GREEN}\nCorrect Password...\n")
        engine.say("Correct Password. Welcome to the Robotic Arm!")
        engine.runAndWait()
        break
    else:
        print(f"{Fore.YELLOW}\nWrong Password")
        engine.say("Wrong Password")
        engine.runAndWait()
        i += 1
        if i < 3:
            print(f"{Fore.CYAN}Try again...")
            engine.say("Try again")
            engine.runAndWait()
        else:
            print(f"{Fore.RED}[Chances Over]")
            engine.say("Chances Over")
            engine.runAndWait()
            sleep(3)
            sys.exit()


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
        print(f"{Fore.RED}[App is going to close]")
        engine.say("App is going to close")
        engine.runAndWait()
        sys.exit()
    if keyboard.is_pressed("a"):
        send("a")
        sleep(0.2)
    if keyboard.is_pressed("s"):
        send("s")
        sleep(0.2)
    if keyboard.is_pressed("d"):
        send("d")
        sleep(0.2)
    if keyboard.is_pressed("f"):
        send("f")
        sleep(0.2)
    if keyboard.is_pressed("w"):
        send("w")
        sleep(0.2)
    if keyboard.is_pressed("r"):
        send("r")
        sleep(0.2)
    if keyboard.is_pressed("e"):
        send("e")
        print(Fore.GREEN + "Automation...")
        engine.say("Automation")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed("z"):
        send("z")
        print(Fore.GREEN + "Arm Moving...")
        engine.say("Arm Moving")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed("c"):
        send("c")
        print(Fore.GREEN + "Clear Data...")
        engine.say("Clear Data")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed("x"):
        send("x")
        print(Fore.GREEN + "Default position...")
        engine.say("Default position")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed("q"):
        send("q")
        print(Fore.GREEN + "Recorded...")
        engine.say("Recorded")
        engine.runAndWait()
        # sleep(1)
