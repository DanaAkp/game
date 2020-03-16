from element.archer import Archer
from element.catapult import Catapult
from element.grass import Grass
from element.horseman import Horseman
from element.swordsman import Swordsman
from element.water import Water
from map.field import Field
from map.player import Player

ground = [Grass('w', 1, 1), Grass('w', 1, 2), Grass('w', 2, 1), Grass('w', 2, 2),
          Water('w', 3, 3), Water('w', 3, 4), Water('w', 4, 3), Water('w', 4, 4)]
units_player1 = [Archer('image/archer_player1', 2, 3), Catapult('image/catapult_player1', 2, 1),
                 Horseman('image/horseman_player1', 4, 1)]
units_player2 = [Archer('image/archer_player2', 4, 2), Catapult('image/catapult_player2', 1, 3),
                 Swordsman('image/swordsman_player2', 1, 1)]

player1 = Player('w', 1, 'name1', units_player1)
player2 = Player('w', 1, 'name2', units_player2)

field = Field(list_ground=ground, list_unit=[units_player1, units_player2])
