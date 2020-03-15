from dataclasses import dataclass
from base.unit import Units
from config.horseman_config import HEALTH, DAMAGE, NAME, MOTION, ATACK_RADIUS

#всадник
@dataclass
class Horseman(Units):
    damage: int = DAMAGE
    health: int = HEALTH
    motion: int = MOTION
    attack_radius: int = ATACK_RADIUS
    name: str = NAME    
