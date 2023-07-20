from Organism import Organism
import random


class Plant(Organism):

    def __init__(self, x, y, strength, initiative, color):
        self.seeds = 0
        super().__init__(x, y, strength, initiative, color)

    def action(self):
        spread_chance = random.randint(0, 10)

        if spread_chance == 0:
            self.seeds += 1

    def plant(self):
        result = self.seeds
        if self.seeds > 0:
            self.seeds -= 1

        return result
