from random import randint, uniform


class Product:
    def __init__(self, name='', price=10, weight=20, flammability=0.5,
                 identifier=uniform(1000000, 9999999)):
                self.name = name
                self.price = price
                self.weight = weight
                self.flammability = flammability
                self.identifier = identifier

    def stealibility(self):
        ratio = self.price/self.weight
        if (ratio < 0.5):
            return "Not so stealable"
        if ((ratio >= 0.5) & (ratio < 1.0)):
            return "kinda stealable"
        else:
            return "Very stealable"

    def explode(self):
        explodability = self.flammability * self.weight
        if (explodability < 10):
            return "...fizzle"
        if((explodability >= 10) & (explodability < 50)):
            return "...boom"
        else:
            return "...BABOOM!"


class BoxingGlove(Product):
    def __init__(self, name='', price=10, weight=10, flammability=0.5,
                 identifier=randint(1000000, 9999999)):
        super().__init__(name=name, price=price,
                         flammability=flammability, identifier=identifier)
        self.weight = weight

    def explode(self):
        return "...it's a glove"

    def punch(self):
        if (self.weight < 5):
            return "That tickles!"
        if ((self.weight >= 5) & (self.weight < 15)):
            return "Hey! That hurt!"
        else:
            return "OUCH!"
