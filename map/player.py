from dataclasses import dataclass

from map.image import Image


@dataclass
class Player(Image):
    ID: int
    name: str
    list_unit: list

    def add_unit(self, unit):
        self.list_unit.append(unit)

    def delete_unit(self, unit):
        self.list_unit.remove(unit)

    # проверить принадлежит ли юнит игроку
    # мб добавить карту в эти поля
    def is_self_unit(self, my_unit):
        if my_unit in self.list_unit:
            return True
        print('Это не ваш юнит!')
        return False

    def move_unit(self, select_unit, x, y, field):
        if not field.is_can_move_unit(x, y) and not select_unit.is_move(x, y):
            print('Действие невозможно!')

    def is_attack_unit(self, attacker, attacked):
        if attacked in self.list_unit:
            print('Эти юниты - друзья!')
            return False
        if attacked.is_dead:
            print('Выбранный юнит мертв!')
            return False
        if not attacker.is_attack(attacked):
            print('Ход невозможен!')
            return False
        return True

    def attack_unit(self, attacker, attacked):
        if self.is_attack_unit(attacker, attacked):
            attacker.attack(attacked)
