class NPC:
    def __init__(self, name, hp, is_hostile):
        self.name: str = name
        self.hp: int = hp
        self.is_hostile: bool = is_hostile

    def change_hp(self, change):
        self.hp = self.hp + change