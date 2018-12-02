class Cell():
    visible = False
    row = -1
    col = -1
    char = ""
    visible = False

    def __init__(self, row, col, char, visible):
        self.row = row
        self.col = col
        self.char = char
        self.visible = visible

    def isVisible(self):
        return self.visible