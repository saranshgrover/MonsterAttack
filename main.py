from game import Game
from map import Map
from cell import Cell
from player import Player

print("Welcome to Monster Attacks!")
filename = "map3.txt"
GameMap = Map("map3.txt")
Game = Game()
Game.reveal_area(GameMap, GameMap.player.row, GameMap.player.col)
move = 0

def print_map():
    for row in GameMap.Grid:
        for cell in row:
            if cell.visible:
                print(cell.char, end="")
            else:
                print(" ", end="")
        print()

def print_player_info():
    print("Hi! Player Health = {} and Coins = {}".format(GameMap.player.player_health, GameMap.player.coins))

while GameMap.player.player_health > 0 and move == 0:
    print_map()
    print_player_info()
    char = input()
    move = 0
    if char == 'w':
        move = Game.player_turn(GameMap, GameMap.player, 'U')
    elif char == 'a':
        move = Game.player_turn(GameMap, GameMap.player, 'L')
    elif char == 's':
        move = Game.player_turn(GameMap, GameMap.player, 'D')
    elif char == 'd':
        move = Game.player_turn(GameMap, GameMap.player, 'R')
    if move == 0:
        Game.reveal_area(GameMap, GameMap.player.row, GameMap.player.col)

print_map()

if GameMap.player.coins >=3 and GameMap.player.player_health > 0:
    print('Congratulations')
else:
    if GameMap.player.player_health <=0:
        print("You died")
    else:
        print("You failed")
print_player_info()

