from Animal import Animal
import pickle


class Human(Animal):
    def __init__(self, x, y):
        self.cooldown = 0
        super().__init__(x, y, 5, 4, 'black')

    def action(self):
        if self.new:
            self.new = False
            return
        self.prev_x = self.x
        self.prev_y = self.y

        if self.cooldown > 0:
            if self.cooldown > 5:
                self.strength -= 1
            self.cooldown -= 1

        hdir = self.world.human_dir

        if hdir == 'w' and self.y > 0:
            self.y -= self.world.box_size
        elif hdir == 's' and self.y < self.world.sym_height * self.world.box_size - self.world.box_size:
            self.y += self.world.box_size
        elif hdir == 'a' and self.x > 0:
            self.x -= self.world.box_size
        elif hdir == 'd' and self.x < self.world.sym_width * self.world.box_size - self.world.box_size:
            self.x += self.world.box_size
        elif hdir == 'space':
            self.__activate_super()

    def __activate_super(self):
        if self.cooldown == 0:
            self.strength = 10
            self.cooldown = 10

    def save(self, file):
        pickle.dump(type(self).__name__, file)
        pickle.dump(self.x, file)
        pickle.dump(self.y, file)
        pickle.dump(self.strength, file)
        pickle.dump(self.cooldown, file)

    def load(self, file):
        self.x = pickle.load(file)
        self.y = pickle.load(file)
        self.strength = pickle.load(file)
        self.cooldown = pickle.load(file)
