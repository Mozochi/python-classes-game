#%%
import random

evil_NPC_types = ["Goblin", "Orc", "Troll", "Dragon", "Giant"]
evil_NPC_dropTable = ["Gold", "Sword", "Shield", "Potion", "Armor"]

friendly_NPC_types = ["Shopkeeper"]
shop_inventory = {"Sword": 10, "Shield": 10, "Potion": 10, "Armor": 10} # Item : Cost


class NPC:
    def __init__(self, name, is_hostile, playerLevel):
        self.name: str = name
        self.is_hostile: bool = is_hostile
        self.playerLevel = playerLevel
        self.inventory = {}
        self.xp = 0

        if self.is_hostile:
            self.name = random.choice(evil_NPC_types)
            self.inventory = {random.choice(evil_NPC_dropTable): 1}
            self.hp = random.randint(self.playerLevel, self.playerLevel + int(self.playerLevel * 1.5))
        else:
            self.name = random.choice(friendly_NPC_types)
            self.inventory = shop_inventory
            self.hp = 100
        

    def change_hp(self, change):
        self.hp = self.hp + change


    def attack(self, target):
        attack_value = random.randint(self.playerLevel, self.playerLevel + int(self.playerLevel * 1.5))
        print(f'{self.name} attacks {target.name} for {attack_value}')
        target.change_hp(attack_value * -1)

    def __del__(self):
        if self.hp <= 0:
            print(f'{self.name} has been defeated!')
            return self.inventory, self.xp
    
#%%
