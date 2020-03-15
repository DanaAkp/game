from base.unit import Unit


class LongRange(Unit):
    def is_attack(self, other):
        dist = self.calculate_distance(other)
        if 1 <= dist < self.attack_radius:
            return True
        return False

    def attack(self, other):
        dist = self.calculate_distance(other)
        if 1 == dist:
            other.damaged(self.damage/2)
        else:
            other.damaged(self.damage)