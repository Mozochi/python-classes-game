class Shop:
    def __init__(self, playerGold, shopInventory):
        self.playerCoins = playerGold
        self.itemsForSale = {}  # item:cost

    def buy_item(self, item):
        if self.playerCoins < self.itemsForSale.get(item):
            print("You do not have enough gold")
            return

        self.itemsForSale.pop(item, None)

        return True
