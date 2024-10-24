from scripts.NPC import NPC




class Grid:
    def __init__(self):
        self.grid = []
        self.gridDict = {}

    def generate_empty_grid(self, size_x, size_y):
        self.grid = [[0 for x in range(size_x)] for y in range(size_y)]
        self.gridDict = {}

    def add_to_grid(self, x, y, item):
        self.grid[x][y] = item
        self.gridDict[item] = (x, y)

    def print_grid(self):
        for row in self.grid:
            for cell in row:
                print(f"|  {str(cell)[:1]}  ", end="")
            print("| \n")

    def move_item(self, x, y, item):
        if item in self.gridDict:
            old_x, old_y = self.gridDict[item]
            self.grid[old_x][old_y] = 0
            self.grid[x][y] = item
            self.gridDict[item] = (x, y)

    def move_right(self, item):
        if item in self.gridDict:
            x, y = self.gridDict[item]
            self.move_item(x, y + 1, item)

    def move_left(self, item):
        if item in self.gridDict:
            x, y = self.gridDict[item]
            self.move_item(x, y - 1, item)

    def move_up(self, item):
        if item in self.gridDict:
            x, y = self.gridDict[item]
            self.move_item(x - 1, y, item)

    def move_down(self, item):
        if item in self.gridDict:
            x, y = self.gridDict[item]
            self.move_item(x + 1, y, item)
    
    def generate_grid(self, playerLevel):

        self.generate_empty_grid(7, 10)
        NPC_list = []
        NPC_location = {} #NPC Name : (x,y)

        Creature: NPC = NPC("Creature", False, playerLevel)
        NPC_list.append(Creature)
        NPC_location[Creature.name] = (3, 3)

        Shop: NPC = NPC("Shopkeeper", False, playerLevel)
        NPC_list.append(Shop)  
        NPC_location[Shop.name] = (3, 4)
        

        self.add_to_grid(3, 3, Creature.name)
        self.add_to_grid(3, 4, Shop.name)
        

        return NPC_list, NPC_location
        