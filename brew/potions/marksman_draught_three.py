from ..potions.potion import *


class MarksmanDraughtThree(Potion):
    def __init__(self, win=None):
        super().__init__(win)
        self.name = "Marksman Draught Three"

    def select(self):
        time.sleep(.2)
        mouse.move(1157, 840)
        mouse.click()
        self.create_past_max()


if __name__ == "__main__":
    potion = MarksmanDraughtThree()
    potion.brew()


