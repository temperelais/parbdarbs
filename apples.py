class Harvest:
    def __init__(self, VegOrFruit, name, howMuch):
        self.VegOrFruit = VegOrFruit
        self.name = name
        self.howMuch = howMuch

    def ateSome(self, howManyEaten):
        self.howMuch-=howManyEaten

class Apple(Harvest):
    def __init__(self, name, howMuch,appleBreed):
        super().__init__("fruit", name, howMuch)
        self.appleBreed = appleBreed

        