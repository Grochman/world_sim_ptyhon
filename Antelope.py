from Animal import Animal
import random


class Antelope(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, 4, 4, 'brown')

    def action(self):
        if self.new:
            self.new = False
            return
        self.prev_x = self.x
        self.prev_y = self.y
        move_dir = random.randint(0, 3)
        if move_dir == 0 and self.x < self.world.sym_width * self.world.box_size - 2*self.world.box_size:
            self.x += self.world.box_size*2
        elif move_dir == 1 and self.x > self.world.box_size:
            self.x -= self.world.box_size*2
        elif move_dir == 2 and self.y < self.world.sym_height * self.world.box_size - 2*self.world.box_size:
            self.y += self.world.box_size*2
        elif self.y > self.world.box_size:
            self.y -= self.world.box_size*2

    def collision(self, other):
        if type(other) == type(self):
            other.x = other.prev_x
            other.y = other.prev_y
            return 4

        escape = random.randint(0, 1)
        if escape == 1:
            up = self.world.is_empty(self.x, self.y - self.world.box_size)
            down = self.world.is_empty(self.x, self.y + self.world.box_size)
            left = self.world.is_empty(self.x - self.world.box_size, self.y)
            right = self.world.is_empty(self.x + self.world.box_size, self.y)

            if left:
                self.x -= self.world.box_size
                return 2
            elif right:
                self.x += self.world.box_size
                return 2
            elif up:
                self.y -= self.world.box_size
                return 2
            elif down:
                self.y += self.world.box_size
                return 2

        if self.strength > other.strength:
            return 0
        else:
            return 1
