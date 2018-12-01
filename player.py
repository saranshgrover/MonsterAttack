class Player():
    player_health = -1
    row = -1
    col = -1
    coins = -1

    def __init__(self, row, col, health, coins):
        self.row = row
        self.player_health = health
        self.col = col
        self.coins = coins
