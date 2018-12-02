import map.py
import player.py

class Game:
    # Part 1
    def __init__(self, Map, Player):

    # Part 2
    def is_valid_cell(map , row, col):
        map_row = map.Row
        map_col = map.Col

        if row < 0 or row >= map_row or col < 0 or col >= map_col:
            return -1
        else:
            return 0

    # Part 3
    def get_cell(map, row, col):
        map_row = map.Row
        map_col = map.Col

        if row < 0 or row >= map_row or col < 0 or col >= map_col:
            return -1
        else:
            temp = map.Grid
            return temp[row][col]

    # Part 4
    def set_cell(map, row, col, char):
        # TODO: Finish part 4