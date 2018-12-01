class Player():
    player_health = -1
    row = -1
    col = -1
    coins = -1
    map

    def __init__(self, row, col, health, coins, Map):
        self.row = row
        self.player_health = health
        self.col = col
        self.coins = coins
        self.map = Map
