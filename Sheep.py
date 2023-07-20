from Animal import Animal


class Sheep(Animal):
    def __init__(self, x, y):
        super().__init__(x, y, 4, 4, 'white')

