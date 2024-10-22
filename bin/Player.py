import random


class Player:
    def __init__(self, name, hp):
        self.name: str = name
        self.hp: int = hp
        self.level = 1
        self.inventory = {"coins": 10}

    def change_hp(self, change):
        self.hp = self.hp + change

    def inventory_add(self, item):
        if self.inventory.get(item, 0) == 0:
            self.inventory[item] = 1
        else:
            self.inventory[item] += 1

    def inventory_remove(self, item):
        if self.inventory.get(item, 0) != 0:
            self.inventory.pop(item, None)
        else:
            return "That item does not exist"

    def attack(self, target):
        if not target.is_hostile:

            userInput = input(f'Are you sure you want to attack {target.name}, they will become hostile (Y/N)').upper()
            if userInput != 'Y':
                return

        attack_value = random.randint(self.level, self.level + 5)
        print(f'You attack {target.name} for {attack_value}')
        target.change_hp(attack_value * -1)