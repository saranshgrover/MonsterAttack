from cell import Cell

class Player(Cell):
    player_health = -1
    coins = -1

    def __init__(self, row, col, coins, player_health):
        Cell.__init__(row, col, '@', True)
        self.player_health = player_health
        self.coins = coins