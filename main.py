from scripts.Player import Player
from scripts.NPC import NPC
from scripts.Shop import Shop
from scripts.Grid import Grid

NPC_array = {}

def main():

    player: Player = Player("Mozochi", 10)  # Name system needs to be added for user to enter name

    gameGrid: Grid = Grid()

    NPC_List = gameGrid.generate_grid(player.level)
    for NPC in NPC_List:
        NPC_array[NPC.name] = NPC
        print(NPC.name)
    

    #gameGrid.generate_empty_grid(7, 10)

    #player: Player = Player("Mozochi", 10)  # Name system needs to be added for user to enter name
    #gameGrid.add_to_grid(0, 0, player.name)

    
    #gameGrid.print_grid()

if __name__ == '__main__':
    main()

