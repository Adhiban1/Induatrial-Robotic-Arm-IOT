from tkinter import *
from tkinter.ttk import *
import serial
from serial.tools import list_ports
from time import sleep
import pyttsx3

x = 0
y = 0
z = 12
r = 0
u = 45
g = 150
root = Tk()
style = Style()
style.configure("TButton", font=("TimesNewRoman", 15, "bold"), foreground="green")
f1 = Frame(root)
f1.pack()

engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)

ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []

for oneport in ports:
    portList.append(str(oneport))

# print(portList)
port_l = Label(f1, text=str(portList), font="TimesNewRoman 12 italic")
port_l.pack()
val_entry = Entry(f1, font="TimesNewRoman 12 bold", width=5)
val_entry.pack(padx=10)
val = ""


def sub():
    global val
    val = val_entry.get()
    serialInst.baudrate = 9600
    for x in portList:
        if x.startswith("COM" + str(val)):
            portVar = "COM" + str(val)
            # print(x)
    serialInst.port = portVar
    serialInst.open()
    val_entry.delete(0, END)


Button(f1, text="SUBMIT", command=sub).pack(pady=10)


l1 = Label(
    f1,
    text=f"X: {x}, Y: {y}, Z: {z}, R: {r}, U: {u}, G: {g}",
    font="TimesNewRoman 20 bold",
)
l1.pack()


def send(i):
    serialInst.write(str(i).encode("utf-8"))


# try:
#     print(serialInst.readline().decode().rstrip())
# except:
#     print("Except")
# import tkinter.font as font


root.title("Robotic Arm")
# myFont = font.Font(family="Helvetica")


def upd():
    l1.configure(text=f"X: {x}, Y: {y}, Z: {z}, R: {r}, U: {u}, G: {g}")


def display(a):
    l2.configure(text=a)


def xi():
    send("d")
    global x
    x += 1
    if x > 24:
        x = 24
    upd()
    display("")
    # sleep(0.2)


def xd():
    send("a")
    global x
    x -= 1
    if x < -24:
        x = -24
    upd()
    display("")
    # sleep(0.2)


def yi():
    send("w")
    global y
    y += 1
    if y > 24:
        y = 24
    upd()
    display("")
    # sleep(0.2)


def yd():
    send("s")
    sleep(0.2)
    global y
    y -= 1
    if y < 0:
        y = 0
    upd()
    display("")
    # sleep(0.2)


def zi():
    send("r")
    global z
    z += 1
    if z > 24:
        z = 24
    upd()
    display("")
    # sleep(0.2)


def zd():
    send("f")
    global z
    z -= 1
    if z < 0:
        z = 0
    upd()
    display("")
    # sleep(0.2)


def ri():
    send("t")
    global r
    r += 1
    if r > 180:
        r = 180
    upd()
    display("")
    # sleep(0.2)


def rd():
    send("g")
    global r
    r -= 1
    if r < 0:
        r = 0
    upd()
    display("")
    # sleep(0.2)


def ui():
    send("y")
    global u
    u += 1
    if u > 180:
        u = 180
    upd()
    display("")
    # sleep(0.2)


def ud():
    send("h")
    global u
    u -= 1
    if u < 0:
        u = 0
    upd()
    display("")
    # sleep(0.2)


def gi():
    send("u")
    global g
    g += 1
    if g > 150:
        g = 150
    upd()
    display("")
    # sleep(0.2)


def gd():
    send("j")
    global g
    g -= 1
    if g < 90:
        g = 90
    upd()
    display("")
    # sleep(0.2)


def default():
    send("x")
    global x, y, z, r, u, g
    x = 0
    y = 0
    z = 12
    r = 0
    u = 45
    g = 150
    upd()
    display("[DEFAULT]")
    engine.say("Default position")
    engine.runAndWait()
    # sleep(0.2)


def automation():
    send("e")
    display("[AUTOMATION]")
    engine.say("Automation")
    engine.runAndWait()


def Record():
    send("q")
    display("[RECORDED]")
    engine.say("Recorded")
    engine.runAndWait()


def Clear():
    send("c")
    display("[CLEARED]")
    engine.say("Cleared")
    engine.runAndWait()


def Move():
    send("z")
    display("[MOVED]")
    engine.say("Moved")
    engine.runAndWait()


f2 = Frame(root)
f2.pack()
b1 = Button(f2, text="X+", command=xi)
b1.pack(side=LEFT, padx=10, pady=10)
Button(f2, text="Y+", command=yi).pack(side=LEFT, padx=10, pady=10)
Button(f2, text="Z+", command=zi).pack(side=LEFT, padx=10, pady=10)

f3 = Frame(root)
f3.pack()
Button(f3, text="X-", command=xd).pack(side=LEFT, padx=10, pady=10)
Button(f3, text="Y-", command=yd).pack(side=LEFT, padx=10, pady=10)
Button(f3, text="Z-", command=zd).pack(side=LEFT, padx=10, pady=10)

f4 = Frame(root)
f4.pack()
Button(f4, text="R+", command=ri).pack(side=LEFT, padx=10, pady=10)
Button(f4, text="U+", command=ui).pack(side=LEFT, padx=10, pady=10)
Button(f4, text="G+", command=gi).pack(side=LEFT, padx=10, pady=10)

f5 = Frame(root)
f5.pack()
Button(f5, text="R-", command=rd).pack(side=LEFT, padx=10, pady=10)
Button(f5, text="U-", command=ud).pack(side=LEFT, padx=10, pady=10)
Button(f5, text="G-", command=gd).pack(side=LEFT, padx=10, pady=10)

f6 = Frame(root)
f6.pack()
Button(f6, text="RECORD", command=Record).pack(side=LEFT, padx=10, pady=10)
Button(f6, text="AUTOMATE", command=automation).pack(side=LEFT, padx=10, pady=10)
Button(f6, text="CLEAR", command=Clear).pack(side=LEFT, padx=10, pady=10)
Button(f6, text="DEFAULT", command=default).pack(side=LEFT, padx=10, pady=10)
Button(f6, text="MOVE", command=Move).pack(side=LEFT, padx=10, pady=10)

f7 = Frame(root)
f7.pack()
l2 = Label(f7, text="", font="TimesNewRoman 15")
l2.pack()


# def print1():
#     print(serialInst.readline().decode().rstrip())


# Button(f7, text="PRINT", command=print1).pack()
root.mainloop()
