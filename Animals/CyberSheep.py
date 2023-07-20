from Animals.Animal import Animal


class CyberSheep(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, 11, 4, "#3bfff2")

    def action(self):
        if len(self.world.pine) == 0:
            super().action()
        else:
            if self.new:
                self.new = False
                return

            self.prev_y = self.y
            self.prev_x = self.x
            target = self.world.pine[0]
            dist = float('inf')
            for p in self.world.pine:
                p_dist = abs(self.x - p.x) + abs(self.y - p.y)
                if p_dist < dist:
                    dist = p_dist
                    target = p
            if target.x > self.x:
                self.x += self.world.box_size
            elif target.x < self.x:
                self.x -= self.world.box_size
            elif target.y > self.y:
                self.y += self.world.box_size
            elif target.y < self.y:
                self.y -= self.world.box_size
