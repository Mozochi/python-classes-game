from bin.Player import Player
from bin.NPC import NPC
from bin.Shop import Shop
from bin.Grid import Grid




if __name__ == '__main__':
    player: Player = Player("Mozochi", 10)  # Name system needs to be added for user to enter name

    Creature: NPC = NPC("Creature", 10, False, player.level)

    
    """newGrid: Grid = Grid()
    newGrid.add_to_grid(2, 2, player.name)
    newGrid.add_to_grid(1,1, Creature.name)
    newGrid.print_grid()
    print("\n")
    print("\n")
    print("\n")
    newGrid.move_up(player.name)
    newGrid.print_grid()"""

    """shop1: Shop = Shop(player.inventory.get("coins"))
    print(shop1.itemsForSale)
    if shop1.buy_item("test Item"):
        player.inventory_add("test Item")
    print(f'Inv: {player.inventory}')
    print(shop1.itemsForSale)
    del shop1"""

