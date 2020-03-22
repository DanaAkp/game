from base.element_field import ElementField
from dataclasses import dataclass


@dataclass
class Grass(ElementField):
    is_move_unit = True
    img = 'C:/Users/Данагуль/Desktop/текущее/ООЯ и С/game/image/grass1.png'
