from tkinter import *
import serial
from serial.tools import list_ports
import sys
import json
import pyttsx3

with open("app.json", "r") as f:
    controls = json.load(f)

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
    global base, sholder, elbow, wristR, wristU, gripper
    k = a.char
    if controls["base_i"] == k:
        base += 1
        if base > 180:
            base = 180
    elif controls["base_d"] == k:
        base -= 1
        if base < 0:
            base = 0
    elif controls["sholder_i"] == k:
        sholder += 1
        if sholder > 180:
            sholder = 180
    elif controls["sholder_d"] == k:
        sholder -= 1
        if sholder < 0:
            sholder = 0
    elif controls["elbow_i"] == k:
        elbow += 1
        if elbow > 135:
            elbow = 135
    elif controls["elbow_d"] == k:
        elbow -= 1
        if elbow < 0:
            elbow = 0
    elif controls["wristR_i"] == k:
        wristR += 1
        if wristR > 180:
            wristR = 180
    elif controls["wristR_d"] == k:
        wristR -= 1
        if wristR < 0:
            wristR = 0
    elif controls["wristU_i"] == k:
        wristU += 1
        if wristU > 180:
            wristU = 180
    elif controls["wristU_d"] == k:
        wristU -= 1
        if wristU < 0:
            wristU = 0
    elif controls["gripper_i"] == k:
        gripper += 1
        if gripper > 150:
            gripper = 150
    elif controls["gripper_d"] == k:
        gripper -= 1
        if gripper < 90:
            gripper = 90
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

    update()


root.bind("<Key>", main)
l2 = Label(root, text="", font=("TimesNewRoman", 10, "bold"), fg="#FF0000")
l2.pack()
root.mainloop()
