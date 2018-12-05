class Cell():
    visible = False
    row = -1
    col = -1
    char = ""
    visible = False

    def __init__(self, row, col, char, visible=False):
        self.row = row
        self.col = col
        self.char = char
        self.visible = visible

    def isVisible(self):
        return self.visible

    def makeVisible(self):
        self.visible = True
