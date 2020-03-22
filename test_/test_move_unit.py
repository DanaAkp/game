import pytest
from map.field import Field
from map.player import Player
from element.grass import Grass

from element.archer import Archer
from element.horseman import Horseman
from element.swordsman import Swordsman
from element.catapult import Catapult


MOVE_POSITION_X = 15
MOVE_POSITION_Y = 15


unit_to_try = ((Archer(14, 14)),
               (Catapult(14, 14)),
               (Horseman(14, 14)),
               (Swordsman(14, 14)))


@pytest.mark.parametrize('unit', unit_to_try)
def test_move_unit(unit):
    field = Field([unit], [Grass(14, 14), Grass(15, 15)])
    player = Player(1, 'name', [unit], field)
    player.move_unit(unit, MOVE_POSITION_X, MOVE_POSITION_Y)
    assert unit.x == MOVE_POSITION_X and unit.y == MOVE_POSITION_Y
