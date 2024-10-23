from scripts.Player import Player
from scripts.NPC import NPC
from scripts.Shop import Shop
from scripts.Grid import Grid

def main():
    gameGrid: Grid = Grid()
    gameGrid.generate_empty_grid(7, 10)

    player: Player = Player("Mozochi", 10)  # Name system needs to be added for user to enter name
    gameGrid.add_to_grid(0, 0, player.name)

    Creature: NPC = NPC("Creature", 10, False, player.level)
    gameGrid.add_to_grid(1, 1, Creature.name)

    gameGrid.print_grid()


if __name__ == '__main__':
    main()

