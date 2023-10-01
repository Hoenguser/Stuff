import os
import random
import msvcrt

def map_gen(row,column):
    map = [['-']*column for i in range (row)]
    map[0][0] = 'P'
    return map

def obj_gen(map,r_K,c_K,r_D,c_D):
    map[r_K][c_K] = 'K'
    map[r_D][c_D] = 'D'
    

def print_map(map):
    for r in range (0,5):
        for c in range (0,10):
            print(map[r][c],end = ' ')
        print()
    

def movement(ch,r_P_new,c_P_new):
    r_P = r_P_new
    c_P = c_P_new
    if ch == 'W':
        r_P_new = max(0,r_P -1)
    elif ch == 'S':
        r_P_new = min(row-1,r_P+1)
    elif ch == 'A':
        c_P_new = max(0,c_P-1)
    elif ch == 'D':
        c_P_new = min(column-1,c_P+1)
    map[r_P_new][c_P_new] = 'P'
    if r_P_new == r_P and c_P_new == c_P:
        map[r_P][c_P] = 'P'
    else:
        map[r_P][c_P] = '-'
    return r_P_new,c_P_new
    
print('== ESCAPE GAME ==')
print('Use W A S D to move (P)layer')
print('Find (K)ey then exit through the (D)oor')
row = 5
column = 10

r_P_new = 0
c_P_new = 0
key_found = False

r_K = random.randint(1,2)
c_K = random.randint(0,9)
r_D = random.randint(3,4)
c_D = random.randint(0,9)

map = map_gen(row,column)
obj_gen(map,r_K,c_K,r_D,c_D)
print_map(map,row,column)

while True:
    # Key input
    ch = msvcrt.getch().decode('utf-8').upper()
    # Move player
    if ch == 'W' or 'A' or 'S' or 'D':
        r_P_new,c_P_new = movement(ch,r_P_new,c_P_new)
    else:
        print('W,A,S,D only')
    # Clear screen
    os.system('cls')
    # Print new map
    print_map(map,row,column)
    # Finding the key
    if r_P_new == r_K and c_P_new == c_K:
        key_found = True
    # End screen when reaching door
    if r_P_new == r_D and c_P_new == c_D:
        if key_found == True:
            print("You win!")
            break
        else:
            print('You lose')
            print('Maybe find the key first?')
            break








