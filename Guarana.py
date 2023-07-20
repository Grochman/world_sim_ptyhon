from Plant import Plant


class Guarana(Plant):
    def __init__(self, x, y):
        super().__init__(x, y, 0, 0, "#ff5eea")

    def colision(self, other):
        other.strength += 3
        return 1
