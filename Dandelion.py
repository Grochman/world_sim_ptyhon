from Plant import Plant
import random


class Dandelion(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, "yellow")

    def action(self):
        spred_chance = random.randint(0, 10)

        for i in range(3):
            if spred_chance == 0:
                self.seeds += 1
