from brew.potions.potion import *


class StingerStew(Potion):
    def __init__(self, win=None):
        super().__init__(win)
        self.name = "Stinger Stew"

    def select(self):
        for _ in range(11):
            mouse.move(1452, 834)
            mouse.click()
            time.sleep(.1)
        time.sleep(.1)
        mouse.move(1145, 670)
        mouse.click()
        time.sleep(.1)
        self.create_past_max()


if __name__ == "__main__":
    potion = StingerStew()
    potion.brew()
