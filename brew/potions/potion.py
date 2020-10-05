import mouse
import keyboard
import time
from window_input import Window, Key
from ..board import Board


class Potion:
    def __init__(self, win):
        self.win = win
        self.name = None
        self.rep = 0
        self.requirements = []
        self.pattern = []

    def select(self):
        pass

    def create_past_max(self):
        if self.win.pixel(1156, 493) == (255, 255, 255):
            time.sleep(.5)
            mouse.move(1208, 574)
            mouse.click()
            time.sleep(.1)
            mouse.release()
        else:
            print(self.win.text)

    def brew(self):
        self.win = Window()
        while self.win.text != "The Legend of Pirates Online [BETA]":
            self.win = Window()
        while not keyboard.is_pressed("`"):
            pass
        else:
            board = Board(self, self.win)
        time.sleep(.5)
        if self.name:
            while True:
                if keyboard.is_pressed("'"):
                    return
                else:
                    self.select()
                    board.solve()

