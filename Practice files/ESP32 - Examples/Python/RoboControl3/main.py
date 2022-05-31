import keyboard
import serial
from serial.tools import list_ports
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

print(Fore.RED + "Controls:")

with open("controls.txt", "r") as f:
    content = f.read()
print(Fore.YELLOW + content)
content = content.split("\n")


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
    if keyboard.is_pressed(content[11][content[11].find(":") + 2 :]):
        print(f"{Fore.RED}[App is going to close]")
        engine.say("App is going to close")
        engine.runAndWait()
        sys.exit()
    if keyboard.is_pressed(content[1][content[1].find(":") + 2 :]):
        send("a")
        sleep(0.2)
    if keyboard.is_pressed(content[3][content[3].find(":") + 2 :]):
        send("s")
        sleep(0.2)
    if keyboard.is_pressed(content[0][content[0].find(":") + 2 :]):
        send("d")
        sleep(0.2)
    if keyboard.is_pressed(content[5][content[5].find(":") + 2 :]):
        send("f")
        sleep(0.2)
    if keyboard.is_pressed(content[2][content[2].find(":") + 2 :]):
        send("w")
        sleep(0.2)
    if keyboard.is_pressed(content[4][content[4].find(":") + 2 :]):
        send("r")
        sleep(0.2)
    if keyboard.is_pressed(content[12][content[12].find(":") + 2 :]):
        send("t")
    if keyboard.is_pressed(content[13][content[13].find(":") + 2 :]):
        send("g")
    if keyboard.is_pressed(content[14][content[14].find(":") + 2 :]):
        send("y")
    if keyboard.is_pressed(content[15][content[15].find(":") + 2 :]):
        send("h")
    if keyboard.is_pressed(content[16][content[16].find(":") + 2 :]):
        send("u")
    if keyboard.is_pressed(content[17][content[17].find(":") + 2 :]):
        send("j")
    if keyboard.is_pressed(content[7][content[7].find(":") + 2 :]):
        send("e")
        print(Fore.GREEN + "Automation...")
        engine.say("Automation")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed(content[8][content[8].find(":") + 2 :]):
        send("z")
        print(Fore.GREEN + "Arm Moving...")
        engine.say("Arm Moving")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed(content[10][content[10].find(":") + 2 :]):
        send("c")
        print(Fore.GREEN + "Clear Data...")
        engine.say("Clear Data")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed(content[9][content[9].find(":") + 2 :]):
        send("x")
        print(Fore.GREEN + "Default position...")
        engine.say("Default position")
        engine.runAndWait()
        # sleep(1)
    if keyboard.is_pressed(content[6][content[6].find(":") + 2 :]):
        send("q")
        print(Fore.GREEN + "Recorded...")
        engine.say("Recorded")
        engine.runAndWait()
        # sleep(1)
