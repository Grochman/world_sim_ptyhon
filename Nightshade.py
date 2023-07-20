from Plant import Plant


class Nightshade(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, 99, 0, "blue")

    def colision(self, other):
        return 0
