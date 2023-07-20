from Plants.Plant import Plant


class Grass(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, "#19e34f")
