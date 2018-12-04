from cell import Cell
from player import Player

class Map():
    File = ''
    Row = 0
    Col = 0
    player_health = coins = -1
    player = Player(0,0,0,0)
    Grid = None

    def __init__(self, File):
        self.file = File
        file_object = open(File, "r")
        self.Row = int(file_object.readline())
        self.Col = int(file_object.readline())
        self.player_health = int(file_object.readline())
        self.coins = int(file_object.readline())
        Grid = [[0 for x in range(self.Col)] for y in range(self.Row)]
        contents = file_object.read()
        counter = 0
        for i in range(self.Row):
            for j in range(self.Col):
                print(i)
                print(j)
                if contents[counter] == '@':
                    self.player = Player(i, j, self.player_health, self.coins)
                    Grid[i][j] = self.player
                else:
                    Grid[i][j] = Cell(i, j, contents[counter], False)






