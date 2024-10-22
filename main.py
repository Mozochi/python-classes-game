from Player import Player
from Shop import Shop
from NPC import NPC

if __name__ == '__main__':
    player: Player = Player("Mozochi", 10)  # Name system needs to be added for user to enter name

    Creature: NPC = NPC("Creature", 10, False)

    """shop1: Shop = Shop(player.inventory.get("coins"))
    print(shop1.itemsForSale)
    if shop1.buy_item("test Item"):
        player.inventory_add("test Item")
    print(f'Inv: {player.inventory}')
    print(shop1.itemsForSale)
    del shop1"""
