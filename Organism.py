import pickle
from abc import ABC, abstractmethod
import World


class Organism(ABC):

    def __init__(self, x, y, strength, initiative, color):
        self.x = x
        self.y = y
        self.strength = strength
        self.initiative = initiative
        self.world = World.World.get_instance()
        self.color = color
        self.sprite = self.world.make_sprite(x, y, color)

    @abstractmethod
    def action(self):
        pass

    def collision(self, other):
        if self.strength > other.strength:
            return 0
        else:
            return 1

    def save(self, file):
        pickle.dump(type(self).__name__, file)
        pickle.dump(self.x, file)
        pickle.dump(self.y, file)
        pickle.dump(self.strength, file)

    def load(self, file):
        self.x = pickle.load(file)
        self.y = pickle.load(file)
        self.strength = pickle.load(file)
