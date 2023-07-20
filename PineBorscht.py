from Plant import Plant
from CyberSheep import CyberSheep


class PineBrost(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, 10, 0, "red")
        self.world.pine.append(self)

    def action(self):
        self.world.kill(self.x-self.world.box_size, self.y)
        self.world.kill(self.x+self.world.box_size, self.y)
        self.world.kill(self.x, self.y-self.world.box_size)
        self.world.kill(self.x, self.y+self.world.box_size)

    def collision(self, other):
        self.world.pine.remove(self)
        if isinstance(other, CyberSheep):
            return 1
        return 0
