from Animal import Animal
import random


class Fox(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, 3, 7, 'orange')

    def action(self):
        if self.new:
            self.new = False
            return
        self.prev_x = self.x
        self.prev_y = self.y

        up = self.world.is_safe(self.x, self.y-self.world.box_size, self.strength)
        down = self.world.is_safe(self.x, self.y+self.world.box_size, self.strength)
        left = self.world.is_safe(self.x-self.world.box_size, self.y, self.strength)
        right = self.world.is_safe(self.x+self.world.box_size, self.y, self.strength)

        move_dir = random.randint(0, 3)
        if move_dir == 0 and self.x < self.world.sym_width * self.world.box_size - self.world.box_size and right:
            self.x += self.world.box_size
        elif move_dir == 1 and self.x > 0 and left:
            self.x -= self.world.box_size
        elif move_dir == 2 and self.y < self.world.sym_height * self.world.box_size - self.world.box_size and down:
            self.y += self.world.box_size
        elif move_dir == 3 and self.y > 0 and up:
            self.y -= self.world.box_size

