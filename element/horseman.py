from dataclasses import dataclass
from base.unit import Unit
from config.horseman_config import HEALTH, DAMAGE, NAME, MOTION, ATTACK_RADIUS

#всадник
@dataclass
class Horseman(Unit):
    damage: int = DAMAGE
    health: int = HEALTH
    motion: int = MOTION
    attack_radius: int = ATTACK_RADIUS
    name: str = NAME    
