class Grid:
    def __init__(self):
        self.grid = [[0 for x in range(5)] for y in range(5)]
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
