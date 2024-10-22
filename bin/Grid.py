class Grid:
    def __init__(self):
        self.grid = [[0 for x in range(5)] for y in range(5)]

    def add_to_grid(self, x, y, item):
        self.grid[x][y] = item;\
        self.playerCoords = (x, y)


    def print_grid(self):
        for row in self.grid:
            for cell in row:
                print(f"|  {str(cell)[:1]}  ", end="")
            print("| \n")

    def move_item(self, x, y, item):
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = 0
        self.playerCoords = (x ,y) + self.playerCoords
        self.grid[x][y] = str(item)[:1]


    def move_right(self, player):
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = 0
        self.playerCoords = (self.playerCoords[0], self.playerCoords[1] + 1)
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = (player.name)[:1]

    def move_left(self, player):
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = 0
        self.playerCoords = (self.playerCoords[0], self.playerCoords[1] - 1)
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = (player.name)[:1]

    def move_up(self, player):
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = 0
        self.playerCoords = (self.playerCoords[0] - 1, self.playerCoords[1])
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = (player.name)[:1]

    def move_down(self, player):
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = 0
        self.playerCoords = (self.playerCoords[0] + 1, self.playerCoords[1])
        self.grid[self.playerCoords[0]][self.playerCoords[1]] = (player.name)[:1]