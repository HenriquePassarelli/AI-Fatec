"""   
    Reference - # https://python.plainenglish.io/coding-the-8-queens-problem-in-python-d168f8df844b

    run - python3 simpler_queen.py
 """

import itertools
from itertools import permutations

lista = list(range(8))
perms = permutations(lista)
for perm in perms:
    print(perm)

table = [[0]*8 for _ in range(8)]

def print_table():
    for row in range(8):
        print(table[row])

def put_queen(x,y):
    if table[y][x] == 0:
        for m in range(8):
            table[y][m] = 1
            table[m][x] = 1
            table[y][x] = 2
            if y+m <= 7 and x+m <= 7:
                table[y+m][x+m] = 1
            if y-m >= 0 and x+m <= 7:
                table[y-m][x+m] = 1
            if y+m <= 7 and x-m >= 0:
                table[y+m][x-m] = 1
            if y-m >= 0 and x-m >= 0:
                table[y-m][x-m] = 1                
        return True

    else:
        return False

lista = list(range(8))
perms = itertools.permutations(lista)

num_comb = 0

for perm in perms:
    if put_queen(perm[0], 0) == True:
        if put_queen(perm[1], 1) == True:
            if put_queen(perm[2], 2) == True:
                if put_queen(perm[3], 3) == True:
                    if put_queen(perm[4], 4) == True:
                        if put_queen(perm[5], 5) == True:
                            if put_queen(perm[6], 6) == True:
                                if put_queen(perm[7], 7) == True:
                                    print_table()
                                    num_comb += 1
                                    print(f"solution{num_comb}")
                                    print(" ")
    table = [[0] * 8 for _ in range(8)]

