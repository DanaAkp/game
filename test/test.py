import pytest
from map.field import Field
from element.grass import Grass

from element.archer import Archer
from element.horseman import Horseman
from element.swordsman import Swordsman
from element.catapult import Catapult


MOVE_POSITION_X = 15
MOVE_POSITION_Y = 15


unit_to_try = ((Archer(14, 14, 1)),
               (Catapult(14, 14, 1)),
               (Horseman(14, 14, 1)),
               (Swordsman(14, 14, 1)))


@pytest.mark.parametrize('unit', unit_to_try)
def test_move_unit(unit):
    field = Field([Grass(14, 14), Grass(15, 15)], [unit])

    gc.move_unit(unit, MOVE_POSITION_X, MOVE_POSITION_Y)
    assert unit.x == MOVE_POSITION_X and unit.y == MOVE_POSITION_Y
