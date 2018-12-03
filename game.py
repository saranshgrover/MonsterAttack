import player
from map import Map
from player import Player
from cell import Cell

class Game:

    map
    player
    # Part 1
    def __init__(self, Filename):
        self.map = Map(Filename)
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
            map.Grid[row][col].char = char

    # Part 5
    def reveal_area(self, map, row, col):
        row -= 1
        col -= 1
        map.Grid[row][col].makeVisible()
        col += 1
        map.Grid[row][col].makeVisible()
        col += 1
        map.Grid[row][col].makeVisible()
        row += 1
        col -= 2
        map.Grid[row][col].makeVisible()
        col += 1
        map.Grid[row][col].makeVisible()
        col += 1
        map.Grid[row][col].makeVisible()
        row += 1
        col -= 2
        map.Grid[row][col].makeVisible()
        col += 1
        map.Grid[row][col].makeVisible()
        col += 1
        map.Grid[row][col].makeVisible()

    # Part 6
    def get_attack_target(self, map, player, direction):
        row = player.Row
        col = player.Col
        if direction == 'U':
            row -= 1
        elif direction == 'D':
            row += 1
        elif direction == 'L':
            col -= 1
        elif direction == 'R':
            col += 1
        else:
            return -1
        if self.is_valid_cell(map,row,col):
            attack_target = map.Grid[row][col].char
            if attack_target == 'm' or attack_target == 'B' or attack_target == '/':
                return attack_target
            else:
                return -1
        else:
            return -1

    # Part 7
    def complete_attack(self, map, player,row,col):
        target_cell = self.get_cell(map,row,col)
        if target_cell == 'm':
            self.set_cell(map,row,col,'$')
            player.player_health -= 1
        elif target_cell == 'B':
            self.set_cell(map, row, col, '*')
            player.player_health -= 2
        elif target_cell == '/':
            self.set_cell(map, row, col, '.')
        if player.player_health <= 0:
            self.set_cell(map,player.row,player.col,'X')
        return

    # Part 8
    def monster_attacks(self,map,player):
        counter = 0
        row = player.row
        col = player.col
        # R-1,C
        row-=1
        cell = self.get_cell(map,row,col)
        if cell == 'm':
            counter += 1
        elif cell == 'B':
            counter += 2
        # R-1,C
        row += 2
        cell = self.get_cell(map, row, col)
        if cell == 'm':
            counter += 1
        elif cell == 'B':
            counter += 2
        # R,C-1
        row-=1
        col-=1
        cell = self.get_cell(map,row,col)
        if cell == 'm':
            counter += 1
        elif cell == 'B':
            counter += 2
        # R,C+1
        col += 2
        cell = self.get_cell(map, row, col)
        if cell == 'm':
            counter += 1
        elif cell == 'B':
            counter += 2
        return counter

    # Part 9
    def player_move(self, map, player, row, col):
        dmgTaken = self.monster_attacks(map, player)
        player.player_health -= dmgTaken
        if player.player_health <= 0:
            player.char = 'X'
            return 0
        targetCell = self.get_cell(map, row, col)
        if targetCell.char == '.':
            temp = player
            player = Cell(player.row, player.col, '.', True)
            targetCell = temp
        elif targetCell.char == '$':
            temp = player
            player = Cell(player.row, player.col, '.', True)
            targetCell = temp
            temp.coins += 1
        elif targetCell.char == '*':
            temp = player
            player = Cell(player.row, player.col, '.', True)
            targetCell = temp
            temp.coins += 5
        elif targetCell.char == '>':
            temp = player
            player = Cell(player.row, player.col, '.', True)
            targetCell = temp
            player.row = row
            player.col = col
            return -1
        player.row = row
        player.col = col
        return 0

    # Part 10
    def player_turn(self, map, player, direction):
        targetRow = player.row
        targetCol = player.col
        if direction == "U":
            targetRow -= 1
        elif direction == "D":
            targetRow += 1
        elif direction == "L":
            targetCol -= 1
        elif direction == "R":
            targetCol += 1
        else:
            return -1
        cell = self.get_cell(map, targetRow, targetCol)
        if not cell:
            return 0
        else:
            attackable = self.get_attack_target(map, player, direction)
            if cell.char == '#':
                return 0
            elif attackable == 'B' or attackable == 'm':
                self.complete_attack(map, player, targetRow, targetCol)
                return 0
            else:
                return self.player_move(map, player, targetRow, targetCol)

