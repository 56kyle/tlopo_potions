from brew.potions.potion import *


class SwiftFootThree(Potion):
    def __init__(self, win=None):
        super().__init__(win)
        self.name = "Swift Foot Three"

    def select(self):
        for _ in range(2):
            mouse.move(1452, 834)
            mouse.click()
            time.sleep(.1)
        mouse.move(1157, 840)
        time.sleep(.1)
        mouse.click()
        time.sleep(.1)
        self.create_past_max()


if __name__ == "__main__":
    potion = SwiftFootThree()
    potion.brew()

