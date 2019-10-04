import unittest
import random


'''
Sprint challenge Part 1
'''


class Product:
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        if (self.price / self.weight) < 0.5:
            return 'Not so stealable'
        elif (self.price / self.weight) < 1:
            return 'Kinda stealable'
        else:
            return 'Very Stealable'

    def explode(self):
        explode_index = self.flammability * self.weight
        if explode_index < 10:
            return '...fizzle.'
        elif explode_index < 50:
            return '...boom!'
        else:
            return '...BABOOM!'


'''
Sprint Challenge Part 3
'''


class BoxingGlove(Product):
    '''
    Boxing Glove subclass of Product
    '''

    def __init__(self, name, weight=10):
        super().__init__(name)
        self.weight = weight

    def explode(self):
        return '...it\'s a glove.'

    def punch(self):
        if self.weight < 5:
            return 'That tickles.'
        elif self.weight < 15:
            return 'Hey that hurt!'
        else:
            return 'OUCH!'
