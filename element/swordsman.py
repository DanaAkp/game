from dataclasses import dataclass
from base.unit import Units
from config.swordsman_config import HEALTH, DAMAGE, NAME, MOTION, ATTACK_RADIUS

#мечник
@dataclass
class Swordsman(Units): 
    damage: int = DAMAGE
    health: int = HEALTH
    motion: int = MOTION
    attack_radius: int = ATTACK_RADIUS
    name: str = NAME    