#https://www.codingame.com/training/easy/power-of-thor-episode-1
#Dominika Stryjewska s16722

import sys
import math

north= "N"
south = "S"
east = "E"
west = "W"
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
    
while True:
    remaining_turns = int(input())
    walk = ""  

    if initial_ty > light_y:
        initial_ty -= 1
        walk += north      
    elif initial_ty < light_y:
        initial_ty += 1
        walk += south

    if initial_tx < light_x:
        initial_tx += 1
        walk += east       
    elif initial_tx > light_x:
        initial_tx -= 1
        walk += west
    
    print(walk)
