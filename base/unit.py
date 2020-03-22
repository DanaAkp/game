from dataclasses import dataclass
from math import sqrt

from base.element_field import ElementField


# from abc import ABCMeta, abstractmethod
# from accessify import protected


@dataclass
class Unit(ElementField):
    is_dead = False

    def __call__(self):
        return '{name}\nЗдоровье: {health}\nКоординаты: ({x},{y})'.format(name=self.name, health=self.health, x=self.x, y=self.y)

    def is_move(self, new_x, new_y):
        if self.is_dead:
            print('Юнит умер!')
            return False
        dist = self.calculate_distance(new_x, new_y)
        if self.motion < dist:
            print('Слишком далеко')
            return False
        return True

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    # @protected
    def damaged(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.is_dead = True

    def is_attack(self, other):
        dist = self.calculate_distance(other)
        if dist == 1:
            return True
        return False

    def attack(self, other):
        other.damaged(self.damage)

    def calculate_distance(self, other):
        return sqrt(pow(self.x - other.x, 2) + pow(self.y - other.y, 2))

    def calculate_distance(self, x, y):
        return sqrt(pow(self.x - x, 2) + pow(self.y - y, 2))
