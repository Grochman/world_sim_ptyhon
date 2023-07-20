from Animal import Animal
import random


class Turtle(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 1, 'green')

    def action(self):
        if self.new:
            self.new = False
            return
        self.prev_x = self.x
        self.prev_y = self.y

        move_dir = random.randint(0, 15)
        if move_dir == 0 and self.x < self.world.sym_width * self.world.box_size - self.world.box_size:
            self.x += self.world.box_size
        elif move_dir == 1 and self.x > 0:
            self.x -= self.world.box_size
        elif move_dir == 2 and self.y < self.world.sym_height * self.world.box_size - self.world.box_size:
            self.y += self.world.box_size
        elif move_dir == 3 and self.y > 0:
            self.y -= self.world.box_size


    def colision(self, other):
        if type(other) == type(self):
            other.x = other.prev_x
            other.y = other.prev_y
            return 4


        if other.strength < 5:  # i jst animal
            other.x = other.prev_x
            other.y = other.prev_y
            return 3

        if self.strength > other.strength:
            return 0
        else:
            return 1
