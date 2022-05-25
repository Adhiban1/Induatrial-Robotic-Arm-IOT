from tkinter import *
import serial
from serial.tools import list_ports
import sys
import json
import pyttsx3
from time import sleep

with open("controls.txt", "r") as f:
    controls = json.loads(f.read())

speech = bool(controls["speech"])

if speech:
    engine = pyttsx3.init()
    engine.setProperty("rate", 150)
    voices = engine.getProperty("voices")
    engine.setProperty("voice", voices[1].id)

    def say(a):
        engine.say(a)
        engine.runAndWait()

else:

    def say(a):
        pass


root = Tk()
root.geometry("1000x500")
root.title("Automated Robotic Arm")
ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()

portList = []
portstr = ""
for oneport in ports:
    portList.append(str(oneport))
    portstr += str(oneport) + "\n"

if portstr == "":
    portstr = "Ports not found"
    say("Ports not found")
l0 = Label(root, text=portstr, font=("TimesNewRoman", 20, "bold"))
l0.pack()
e1 = Entry(root, width=5, font=("TimesNewRoman", 20, "bold"))
e1.pack(padx=5, pady=5)


def comport():
    if portstr == "Ports not found":
        sys.exit()
    else:
        global val
        val = e1.get()
        for x in portList:
            if x.startswith("COM" + str(val)):
                portVar = "COM" + str(val)
        serialInst.baudrate = 9600
        serialInst.port = portVar
        serialInst.open()
        l0.configure(text="---Connected---\n", fg="#00FF00")
        root.bind("<Key>", main)
        say("Connected")
        e1.forget()
        b1.forget()


if portstr == "Ports not found":
    b1Name = "EXIT"
else:
    b1Name = "SUBMIT"

b1 = Button(
    text=b1Name,
    command=comport,
    bg="#0000FF",
    fg="#FFFFFF",
    font=("TimesNewRoman", 20, "bold"),
)
b1.pack(padx=5, pady=5)

base = 0
sholder = 135
elbow = 135
wristR = 0
wristU = 45
gripper = 150

baseList = []
sholderList = []
elbowList = []
wristR_List = []
wristU_List = []
gripperList = []

l1 = Label(
    text=f"\nBase: {base}, Sholder: {sholder}, Elbow: {elbow}\nWristR: {wristR}, WristU: {wristU}, Gripper: {gripper}",
    font=("TimesNewRoman", 20, "bold"),
)
l1.pack(padx=5, pady=5)
if portstr == "Ports not found":
    l1.configure(text="")


def update():
    l1.configure(
        text=f"\nBase: {base}, Sholder: {sholder}, Elbow: {elbow}\nWristR: {wristR}, WristU: {wristU}, Gripper: {gripper}"
    )


def display(a):
    l2.configure(text=a)


def send(i):
    serialInst.write(str(i).encode("utf-8"))


def main(a):
    global base, sholder, elbow, wristR, wristU, gripper, baseList, sholderList, elbowList, wristR_List, wristU_List, gripperList
    k = a.char
    if controls["base_i"] == k:
        base += 1
        if base > 180:
            base = 180
        display("")
    elif controls["base_d"] == k:
        base -= 1
        if base < 0:
            base = 0
        display("")
    elif controls["sholder_i"] == k:
        sholder += 1
        if sholder > 180:
            sholder = 180
        display("")
    elif controls["sholder_d"] == k:
        sholder -= 1
        if sholder < 0:
            sholder = 0
        display("")
    elif controls["elbow_i"] == k:
        elbow += 1
        if elbow > 135:
            elbow = 135
        display("")
    elif controls["elbow_d"] == k:
        elbow -= 1
        if elbow < 0:
            elbow = 0
        display("")
    elif controls["wristR_i"] == k:
        wristR += 1
        if wristR > 180:
            wristR = 180
        display("")
    elif controls["wristR_d"] == k:
        wristR -= 1
        if wristR < 0:
            wristR = 0
        display("")
    elif controls["wristU_i"] == k:
        wristU += 1
        if wristU > 180:
            wristU = 180
        display("")
    elif controls["wristU_d"] == k:
        wristU -= 1
        if wristU < 0:
            wristU = 0
        display("")
    elif controls["gripper_i"] == k:
        gripper += 1
        if gripper > 150:
            gripper = 150
        display("")
    elif controls["gripper_d"] == k:
        gripper -= 1
        if gripper < 90:
            gripper = 90
        display("")
    elif controls["default"] == k:
        base = 0
        sholder = 135
        elbow = 135
        wristR = 0
        wristU = 45
        gripper = 150
        display("[DEFAULT]")
        say("Default position")
    elif controls["move"] == k:
        display("[MOVE]")
        send(f"{base:3d}{sholder:3d}{elbow:3d}{wristR:3d}{wristU:3d}{gripper:3d}")
        say("Arm Moved")
    elif controls["record"] == k:
        baseList.append(base)
        sholderList.append(sholder)
        elbowList.append(elbow)
        wristR_List.append(wristR)
        wristU_List.append(wristU)
        gripperList.append(gripper)
        display(f"[RECORD][{len(baseList)}]")
        say(f"Recorded: {len(baseList)}")
    # elif controls["clear"] == k:
    elif "\x08" == k:
        display("[CLEAR]")
        baseList = []
        sholderList = []
        elbowList = []
        wristR_List = []
        wristU_List = []
        gripperList = []
        say("Clear data")
    # elif controls["Automate"] == k:
    elif "\r" == k:
        say("Automation")
        no_of_automations = 3
        display("AUTOMATE")
        for _ in range(no_of_automations):
            for a0, a1, a2, a3, a4, a5 in zip(
                baseList, sholderList, elbowList, wristR_List, wristU_List, gripperList
            ):
                send(f"{a0:3d}{a1:3d}{a2:3d}{a3:3d}{a4:3d}{a5:3d}")
                sleep(2.5)
        display("Automation completed")
        say("Automation completed")
    elif "\x1b" == k:
        sys.exit()

    update()


l2 = Label(root, text="", font=("TimesNewRoman", 10, "bold"), fg="#FF0000")
l2.pack()
root.mainloop()
