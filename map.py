class Map():
    File = ''
    Row = 0
    Col = 0
    Grid = [[]]

    def __init__(self, File):
        self.file = File
        file_object = open(File, "r")
        self.Row = int(file_object.readline())
        self.Col = int(file_object.readline())
        Grid = [[0 for x in range(self.Row)] for y in range(self.Col)]
        contents = file_object.read()
        i = j = 0
        for char in contents:
            if j >= self.Col:
                j = 0
                i += 1
            Grid[i][j] = char
            j += 1




