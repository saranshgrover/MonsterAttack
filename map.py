from cell import Cell
from player import Player

class Map():
    File = ''
    Row = 0
    Col = 0
    player_health = coins = -1
    player = Player(0,0,0,0)
    Grid = [[]]

    def __init__(self, File):
        self.file = File
        file_object = open(File, "r")
        self.Row = int(file_object.readline())
        self.Col = int(file_object.readline())
        self.player_health = int(file_object.readline())
        self.coins = int(file_object.readline())
        Grid = [[0 for x in range(self.Col)] for y in range(self.Row)]
        contents = file_object.read().splitlines()
        for i in range(self.Row):
            for j in range(self.Col):
                #print("{} {}: {}".format(i, j, contents[i][j]))
                if contents[i][j] == '@':
                    print(contents[i][j])
                    print(i)
                    print(j)
                    self.player = Player(i, j, self.player_health, self.coins)
                    Grid[i][j] = self.player
                else:
                    #print(contents[counter])
                    Grid[i][j] = Cell(i, j, contents[i][j], False)





