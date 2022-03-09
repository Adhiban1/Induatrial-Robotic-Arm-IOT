import math
import time
import threading
import random

# point: Place  of the object
# 'point_to_angles2D' is a function which convets the point value into angles a1 and a2
# length: Length if the each arm, Total Arm Length = 2 * length
def point_to_angles2D(point=(0, 1), length=1) -> tuple:
    dis = math.sqrt(point[0] ** 2 + point[1] ** 2)
    if dis < length * 2:
        a1 = math.acos(point[0] / dis) + math.acos(dis / (2 * length))
        a2 = math.pi - 2 * math.acos(dis / (2 * length))
        return (a1 * (180 / math.pi), a2 * (180 / math.pi))
    else:
        print(f'"Out of Range" for point={point} and length={length}')
        return (150, 60)  # Default Value


# 'degrees_to_duty' function converts our given degree into duty, then servo rotates at given angle.
# min_duty and max_duty may vary for different servo.
# You can change min_degrees and max_degrees as your wish.
class degreesToDuty:
    def __init__(self, min_duty=2500, max_duty=8050, min_degrees=0, max_degrees=180):
        self.min_duty = min_duty
        self.max_duty = max_duty
        self.min_degrees = min_degrees
        self.max_degrees = max_degrees

    def degrees_to_duty(self, degrees):
        # increment value per degree
        duty_step = (self.max_duty - self.min_duty) / self.max_degrees

        if degrees > self.max_degrees:
            degrees = self.max_degrees
        elif degrees < self.min_degrees:
            degrees = self.min_degrees

        # Get the duty value for the degrees
        duty = math.floor((duty_step * degrees) + self.min_duty)

        # Check value not out of bounds
        if duty > self.max_duty:
            duty = self.max_duty
        elif duty < self.min_duty:
            duty = self.min_duty

        return duty


# point: Place  of the object
# 'point_to_angles3D' is a function which convets the point value into angles a0, a1 and a2
# length: Length if the each arm, Total Arm Length = 2 * length
def point_to_angles3D(point=(1, 1, 1), l=1):  # 3D point, length -> 3 angles
    if point[0] == 0 and point[1] == 0:
        d1 = math.sqrt(0.01**2 + 0.01**2)
    else:
        d1 = math.sqrt(point[0] ** 2 + point[1] ** 2)
    d2 = math.sqrt(point[0] ** 2 + point[1] ** 2 + point[2] ** 2)
    if d2 < 2 * l:
        a0 = math.acos(point[0] / d1)
        a1 = math.acos(d1 / d2) + math.acos(d2 / (2 * l))
        a2 = math.pi - 2 * math.acos(d2 / (2 * l))

        return (a0 * (180 / math.pi), a1 * (180 / math.pi), a2 * (180 / math.pi))
        # output degree
    else:
        print(f'"Out of Range" for point={point} and length={l}')

        return (None, None, None)  # Default Position


def lock_object():
    global change
    global a5
    a5 = "45 lock the object"
    change = False

    def lock_release():
        global a5
        if a5 == "45 lock the object":
            a5 = "180 release the object"
        elif a5 == "180 release the object":
            a5 = "45 lock the object"

    def angle():
        global change
        while True:
            if change == True:
                lock_release()
                change = False

    def thread1():
        global change
        while True:
            inp = input("Change (c/n): ")
            if inp.lower() == "c":
                change = True
                time.sleep(0.001)
                print(a5 + "\n")
            elif inp.lower() == "n":
                print("No change", a5, "\n")

    thread = threading.Thread(target=thread1)
    thread.start()
    angle()


# changing wrist angle up and down
def wristUpDown(a1, a2):  # Input is Degree
    return 360 - a1 - a2


def randompoint_genarator(
    From=1.5, To=2, l=1
):  # from this distance to that distance ["From" & "To"]
    while True:
        x = round(random.uniform(-2 * l, 2 * l), 2)
        y = round(random.uniform(0, 2 * l), 2)
        z = round(random.uniform(0, 2 * l), 2)
        d = math.sqrt(x**2 + y**2 + z**2)
        if From < d < To:
            break
    return (x, y, z)


# main Function
def main():
    # Angle1, Angle2 = point_to_angles2D((1, 1), 1)
    # print(f"Angle1 is {int(Angle1)} and Angle2 is {int(Angle2)}")

    # Angle1, Angle2 = point_to_angles2D((2, 2), 1)
    # print(f"Angle1 is {int(Angle1)} and Angle2 is {int(Angle2)}")

    # Angle0, Angle1, Angle2 = point_to_angles3D((0, 0, 1.99), 1)
    # print(
    #     "Angle0 is {:5.2f}, Angle1 is {:5.2f} and Angle2 is {:5.2f}".format(
    #         Angle0, Angle1, Angle2
    #     )
    # )

    point = randompoint_genarator()
    # point = (1, 1, 1)
    a0, a1, a2 = point_to_angles3D(point)
    print(a0, a1, a2, wristUpDown(a1, a2))


if __name__ == "__main__":
    main()
