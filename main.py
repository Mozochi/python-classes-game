from scripts.Player import Player
from scripts.NPC import NPC
from scripts.Shop import Shop
from scripts.Grid import Grid

NPC_array = {}
NPC_locations = {}

def main():

    player: Player = Player("Mozochi", 10)  # Name system needs to be added for user to enter name

    gameGrid: Grid = Grid()

    NPC_List, NPC_Locations = gameGrid.generate_grid(player.level)
    for NPC in NPC_List:
        NPC_array[NPC.name] = NPC

    gameGrid.print_grid()


    

    #gameGrid.generate_empty_grid(7, 10)

    #player: Player = Player("Mozochi", 10)  # Name system needs to be added for user to enter name
    #gameGrid.add_to_grid(0, 0, player.name)

    
    #gameGrid.print_grid()

if __name__ == '__main__':
    main()

