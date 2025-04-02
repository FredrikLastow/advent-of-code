import sys
from pprint import pprint

with open(f"2023/8/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    dirs = lines[0]
    coords = dict()

    for line in lines[2:]:
        line = line.split(" = ")

        coord = line[0]
        turns = line[1].split(", ")

        left = turns[0][1:]
        right = turns[1][:-1]

        coords[coord] = (left, right)

    cur_c = 'AAA'
    dir_i = 0
    turns = 0
    while cur_c != 'ZZZ':
        d = dirs[dir_i]
        if d == "L":
            cur_c = coords[cur_c][0]
            turns = turns + 1
            print(d, cur_c)
        elif d == "R":
            cur_c = coords[cur_c][1]
            turns = turns + 1
            print(d, cur_c)

        if dir_i == len(dirs) - 1:
            dir_i = 0
        else:
            dir_i = dir_i + 1 

print(turns, file=sys.stderr)
