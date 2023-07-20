from Organism import Organism
import random

class Plant(Organism):

    def __init__(self, x, y, strength, iniciative, color):
        self.seeds = 0
        super().__init__(x, y, strength, iniciative, color)

    def action(self):
        spred_chance = random.randint(0,10)

        if spred_chance == 0:
            self.seeds += 1

    def plant(self):
        result = self.seeds
        if self.seeds > 0:
            self.seeds -= 1

        return result
