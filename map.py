from cell import Cell
from player import Player

class Map():
    File = ''
    Row = 0
    Col = 0
    player_health = coins = -1
    Grid = [[]]
    player = Player(0,0,0,0)

    def __init__(self, File):
        self.file = File
        file_object = open(File, "r")
        self.Row = int(file_object.readline())
        self.Col = int(file_object.readline())
        self.player_health = int(file_object.readline())
        self.coins = int(file_object.readline())
        Grid = [[0 for x in range(self.Row)] for y in range(self.Col)]
        contents = file_object.read()
        i = j = 0
        for char in contents:
            if j >= self.Col:
                j = 0
                i += 1
            if char == '@':
                self.player = Player(i, j, self.player_health, self.coins)
                Grid.insert([i][j],self.player)
            else:
                Grid.insert([i][j], Cell(i, j, char, False))
            j += 1




