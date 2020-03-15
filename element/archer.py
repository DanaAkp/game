from dataclasses import dataclass
from base.long_range import LongRange
from config.archer_config import HEALTH, DAMAGE, NAME, MOTION, ATACK_RADIUS
#лучник

@dataclass
class Archer(LongRange):
    damage: int = DAMAGE
    health: int = HEALTH
    motion: int = MOTION
    attack_radius: int = ATACK_RADIUS
    name: str = NAME