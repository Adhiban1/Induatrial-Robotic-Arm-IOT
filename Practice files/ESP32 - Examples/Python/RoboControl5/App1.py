from tkinter import *
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
f1 = Frame(root)
f1.pack()


ports = serial.tools.list_ports.comports()
serialInst = serial.Serial()
portList = []
portlistStr = ""
for oneport in ports:
    portList.append(str(oneport))
    portlistStr += str(oneport) + "\n"

# print(portList)
port_l = Label(f1, text=portlistStr, font="TimesNewRoman 12 italic")
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
    port_l.configure(text="")


Button(
    f1,
    text="SUBMIT",
    command=sub,
    bg="#FF0000",
    width=10,
    height=1,
    font=("TimesNewRoman", 10, "bold"),
).pack(pady=10)


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


engine = pyttsx3.init()
engine.setProperty("rate", 150)
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)


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


button_font_size = 10
b1_color = "#00FF00"
b1_width = 8
f2 = Frame(root)
f2.pack()
b1 = Button(
    f2,
    text="X+",
    command=xi,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
)
b1.pack(side=LEFT, padx=10, pady=10)
Button(
    f2,
    text="Y+",
    command=yi,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f2,
    text="Z+",
    command=zi,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)

f3 = Frame(root)
f3.pack()
Button(
    f3,
    text="X-",
    command=xd,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f3,
    text="Y-",
    command=yd,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f3,
    text="Z-",
    command=zd,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)

f4 = Frame(root)
f4.pack()
Button(
    f4,
    text="R+",
    command=ri,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f4,
    text="U+",
    command=ui,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f4,
    text="G+",
    command=gi,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)

f5 = Frame(root)
f5.pack()
Button(
    f5,
    text="R-",
    command=rd,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f5,
    text="U-",
    command=ud,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f5,
    text="G-",
    command=gd,
    bg=b1_color,
    width=b1_width,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)

f6 = Frame(root)
f6.pack()

Button(
    f6,
    text="RECORD",
    command=Record,
    bg="#0000FF",
    fg="#FFFFFF",
    width=10,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f6,
    text="AUTOMATE",
    command=automation,
    bg="#FF00FF",
    fg="#FFFFFF",
    width=10,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f6,
    text="CLEAR",
    command=Clear,
    fg="#FFFFFF",
    bg="#FF0000",
    width=10,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f6,
    text="DEFAULT",
    command=default,
    fg="#FFFFFF",
    bg="#808000",
    width=10,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)
Button(
    f6,
    text="MOVE",
    command=Move,
    fg="#FFFFFF",
    bg="#00FFFF",
    width=10,
    height=1,
    font=("TimesNewRoman", button_font_size, "bold"),
).pack(side=LEFT, padx=10, pady=10)

f7 = Frame(root)
f7.pack()
l2 = Label(f7, text="", font="TimesNewRoman 15")
l2.pack()


# def print1():
#     print(serialInst.readline().decode().rstrip())


# Button(f7, text="PRINT", command=print1).pack()
root.mainloop()
