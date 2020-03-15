from dataclasses import dataclass
from base.long_range import LongRange
from config.catapult_config import HEALTH, DAMAGE, NAME, MOTION, ATACK_RADIUS
   
#катапульта
@dataclass
class Catapult(LongRange):
    damage: int = DAMAGE
    health: int = HEALTH
    motion: int = MOTION
    attack_radius: int = ATACK_RADIUS
    name: str = NAME
