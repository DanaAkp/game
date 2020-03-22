from element.archer import Archer
from element.catapult import Catapult
from element.grass import Grass
from element.horseman import Horseman
from element.swordsman import Swordsman
from element.water import Water
from map.field import Field
from map.player import Player
from test_.test_move_unit import test_move_unit, unit_to_try


units_player1 = [Archer(2, 3), Catapult(2, 1),
                 Horseman(4, 1)]
units_player2 = [Archer(4, 2), Catapult(1, 3),
                 Swordsman(1, 1)]

field = Field(list_ground=Field.fill_field(), list_unit=units_player2+units_player1)
# player1 = Player(1, 'name1', units_player1, field)
# player2 = Player(1, 'name2', units_player2, field)
# for i in field.list_ground:
#     print(i)
# print(field.list_ground)
# x = Archer(1, 2)
#
# s = x()
# print(s)