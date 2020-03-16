from dataclasses import dataclass
from base.long_range import LongRange
from config.archer_config import HEALTH, DAMAGE, NAME, MOTION, ATTACK_RADIUS


@dataclass
class Archer(LongRange):
    damage: int = DAMAGE
    health: int = HEALTH
    motion: int = MOTION
    attack_radius: int = ATTACK_RADIUS
    name: str = NAME
