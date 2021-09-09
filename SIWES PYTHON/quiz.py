import random
import sys
board = [i for i in range(0,9)]
moves = ((1,7,3,9),(5),(2,4,6,8))
winners = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
tab = range(1,10)
def print_board():
    x = 1
    for i in board:
        end = " | "
        if x % 3 == 0:
            end = "\n"
            if i != 1: end+='________\n' ;
            char = ''
            if i in ('x','0'):
                if random.randit(0,1) = 0:
                    return chars
def can_move(brd, player, move):
if move in tab and brd [move-1]== move-1:
places = []
x = 0
for                 