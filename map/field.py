from dataclasses import dataclass
from random import randint

from config.window_config import SIZE_FIELD
from element.grass import Grass
# from base.unit import Units
# from base.ground import Ground
# from image import Image
from element.water import Water


@dataclass
class Field:
    list_unit: list
    list_ground: list

    def is_can_move_unit(self, x, y):
        for un in self.list_unit:
            if un.x == x and un.y == y:
                return False
        for gr in self.list_ground:
            if not gr.is_move_unit:
                if gr.x == x and gr.y == y:
                    return False
        return True

    @staticmethod
    def fill_field():
        ground = []
        for i in range(SIZE_FIELD):
            for j in range(SIZE_FIELD):
                ground.append(Grass(i, j))

        for k in range(randint(5, SIZE_FIELD)):
            i = randint(1, len(ground) - 1)
            ground[i] = Water(ground[i].x, ground[i].y)
        return ground
