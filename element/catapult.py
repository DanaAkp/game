from dataclasses import dataclass
from base.long_range import LongRange
from config.catapult_config import HEALTH, DAMAGE, NAME, MOTION, ATTACK_RADIUS
   
#катапульта
@dataclass
class Catapult(LongRange):
    damage: int = DAMAGE
    health: int = HEALTH
    motion: int = MOTION
    attack_radius: int = ATTACK_RADIUS
    name: str = NAME
    img = 'C:/Users/Данагуль/Desktop/текущее/ООЯ и С/game/image/catapult.png'
