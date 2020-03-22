from dataclasses import dataclass

from base.unit import Unit
from config.swordsman_config import HEALTH, DAMAGE, NAME, MOTION, ATTACK_RADIUS


# мечник
@dataclass
class Swordsman(Unit):
    damage: int = DAMAGE
    health: int = HEALTH
    motion: int = MOTION
    attack_radius: int = ATTACK_RADIUS
    name: str = NAME
    img = 'C:/Users/Данагуль/Desktop/текущее/ООЯ и С/game/image/swordsman.png'
