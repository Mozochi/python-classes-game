class Shop:
    def __init__(self, playerGold):
        self.playerCoins = playerGold
        self.itemsForSale = {"test Item": 10}  # item:cost

    def buy_item(self, item):
        if self.playerCoins < self.itemsForSale.get(item):
            print("You do not have enough gold")
            return



        self.itemsForSale.pop(item, None)

        return True
