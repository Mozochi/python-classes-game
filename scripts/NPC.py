import random


class NPC:
    def __init__(self, name, hp, is_hostile, playerLevel):
        self.name: str = name
        self.hp: int = hp
        self.is_hostile: bool = is_hostile
        self.playerLevel = playerLevel

    def change_hp(self, change):
        self.hp = self.hp + change

    def attack(self, target):
        attack_value = random.randint(self.playerLevel, self.playerLevel + int(self.playerLevel * 1.5))
        print(f'{self.name} attacks {target.name} for {attack_value}')
        target.change_hp(attack_value * -1)