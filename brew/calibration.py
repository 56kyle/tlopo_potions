import collections
from window_input import Window, Key
import keyboard
import time

Point = collections.namedtuple("Point", "x y")


column_checks = [
    Point(x=1002, y=72),
    Point(x=1082, y=114),
    Point(x=1154, y=74),
    Point(x=1224, y=114),
    Point(x=1294, y=72),
    Point(x=1366, y=114),
    Point(x=1436, y=72),
    Point(x=1504, y=114)
]


if __name__ == "__main__":
    time.sleep(2)
    win = Window()
    new_values = []
    for location in column_checks:
        while not keyboard.is_pressed("`"):
            pass
        else:
            new_values.append(win.pixel(location))
            time.sleep(.5)
    print("[")
    for value in new_values:
        print("    Color(r={}, g={}, b={}),".format(*value))
    print("]")

