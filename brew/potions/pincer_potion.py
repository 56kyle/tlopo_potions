from brew.potions.potion import *


class PincerPotion(Potion):
    def __init__(self, win=None):
        super().__init__(win)
        self.name = "Pincer Potion"

    def select(self):
        for _ in range(11):
            mouse.move(1452, 834)
            mouse.click()
            time.sleep(.1)
        time.sleep(.1)
        mouse.move(1151, 732)
        mouse.click()
        self.create_past_max()


if __name__ == "__main__":
    potion = PincerPotion()
    potion.brew()
