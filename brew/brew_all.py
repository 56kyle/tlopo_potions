from brew.potions.cannon_draft_three import CannoneerDraftThree
from brew.potions.swift_foot_three import SwiftFootThree
from brew.potions.marksman_draught_three import MarksmanDraughtThree
from brew.potions.pincer_potion import PincerPotion
from brew.potions.gator_grog import GatorGrog
from brew.potions.stinger_stew import StingerStew


if __name__ == "__main__":
    cannon = CannoneerDraftThree()
    swift = SwiftFootThree()
    marks = MarksmanDraughtThree()
    stew = StingerStew()
    pot = PincerPotion()
    grog = GatorGrog()
    queue = [
        cannon,
        swift,
        marks,
        stew,
        pot,
        grog
    ]

    while True:
        for potion in queue:
            potion.brew()

