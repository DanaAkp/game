from map.player import Player
from map.field import Field

from element.archer import Archer
from element.catapult import Catapult
from element.horseman import Horseman
from element.swordsman import Swordsman

from element.water import Water
from element.grass import Grass


ground = [Grass('w', 1, 1), Grass('w', 1, 2), Grass('w', 2, 1), Grass('w', 2, 2),
          Water('w', 3, 3), Water('w', 3, 4), Water('w', 4, 3), Water('w', 4, 4)]
units_player1 = [Archer('e', 2, 3), Catapult('e', 2, 1), Horseman('e', 4, 1)]
units_player2 = [Archer('e', 4, 2), Catapult('e', 1, 3), Swordsman('e', 1, 1)]

player1 = Player('w', 1, 'name1', units_player1)
player2 = Player('w', 1, 'name2', units_player2)

field = Field(list_ground=ground, list_unit=[units_player1,units_player2])