from dataclasses import dataclass

from map.coordinates import Coordinates
from map.image import Image


@dataclass
class ElementField(Coordinates, Image):
    is_move_unit = False