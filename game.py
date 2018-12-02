from map import Map
from player import Player
from cell import Cell

class Game:
    # Part 1
    def __init__(self, Map, Player):

    # Part 2
    def is_valid_cell(self, map, row, col):
        map_row = map.Row
        map_col = map.Col

        if row < 0 or row >= map_row or col < 0 or col >= map_col:
            return False
        else:
            return True

    # Part 3
    def get_cell(self, map, row, col):
        map_row = map.Row
        map_col = map.Col

        if row < 0 or row >= map_row or col < 0 or col >= map_col:
            return False
        else:
            temp = map.Grid
            return temp[row][col]

    # Part 4
    def set_cell(self, map, row, col, char):
        if self.is_valid_cell(map, row, col):
            temp = map.Grid[row][col]
