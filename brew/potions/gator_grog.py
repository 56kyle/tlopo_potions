from brew.potions.potion import *


class GatorGrog(Potion):
    def __init__(self, win=None):
        super().__init__(win)
        self.name = "Gator Grog"

    def select(self):
        for _ in range(11):
            mouse.move(1452, 834)
            mouse.click()
            time.sleep(.1)
            mouse.release()
            time.sleep(.1)
        time.sleep(.1)
        mouse.move(1151, 702)
        mouse.click()
        time.sleep(.1)
        mouse.release()
        self.create_past_max()


if __name__ == "__main__":
    potion = GatorGrog()
    potion.brew()
