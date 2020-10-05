from ..potions.potion import *


class CannoneerDraftThree(Potion):
    def __init__(self, win=None):
        super().__init__(win)
        self.name = "Cannoneer Draft Three"

    def select(self):
        for _ in range(2):
            mouse.move(1452, 834)
            mouse.click()
            time.sleep(.1)
            mouse.release()
            time.sleep(.1)
        time.sleep(.1)
        mouse.move(1159, 768)
        mouse.click()
        time.sleep(.1)
        mouse.release()
        self.create_past_max()


if __name__ == "__main__":
    potion = CannoneerDraftThree()
    potion.brew()


