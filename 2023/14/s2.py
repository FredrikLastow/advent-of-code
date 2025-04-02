import sys
from pprint import pprint
from tqdm import tqdm

def north(cols):
    tilted_cols = ["" for l in range(len(cols[0]))]
    for i, col in enumerate(cols):
        cur_stone = ""
        cur_dot = ""
        for j, c in enumerate(col):
            if c == "O":
                cur_stone = cur_stone + c
            elif c == ".":
                cur_dot = cur_dot + c
            elif c == "#":
                tilted_cols[i] = tilted_cols[i] + cur_stone + cur_dot + "#"
                cur_dot = ""
                cur_stone = ""
            
            if j == len(cols) -1:
                tilted_cols[i] = tilted_cols[i] + cur_stone + cur_dot

    return tilted_cols

def west(rows):
    tilted_rows = ["" for l in range(len(rows[0]))]
    for i, row in enumerate(rows):
        cur_stone = ""
        cur_dot = ""
        for j, c in enumerate(row):
            if c == "O":
                cur_stone = cur_stone + c
            elif c == ".":
                cur_dot = cur_dot + c
            elif c == "#":
                tilted_rows[i] = tilted_rows[i] + cur_stone + cur_dot + "#"
                cur_dot = ""
                cur_stone = ""
            
            if j == len(rows) -1:
                tilted_rows[i] = tilted_rows[i] + cur_stone + cur_dot

    return tilted_rows

def south(cols):
    tilted_cols = ["" for l in range(len(cols[0]))]
    for i, col in enumerate(cols):
        cur_stone = ""
        cur_dot = ""
        for j, c in enumerate(col):
            if c == "O":
                cur_stone = cur_stone + c
            elif c == ".":
                cur_dot = cur_dot + c
            elif c == "#":
                tilted_cols[i] = tilted_cols[i] + cur_dot + cur_stone  + "#"
                cur_dot = ""
                cur_stone = ""
            
            if j == len(cols) -1:
                tilted_cols[i] = tilted_cols[i] + cur_dot + cur_stone

    return tilted_cols

def east(rows):
    tilted_rows = ["" for l in range(len(rows[0]))]
    for i, row in enumerate(rows):
        cur_stone = ""
        cur_dot = ""
        for j, c in enumerate(row):
            if c == "O":
                cur_stone = cur_stone + c
            elif c == ".":
                cur_dot = cur_dot + c
            elif c == "#":
                tilted_rows[i] = tilted_rows[i] + cur_dot + cur_stone + "#"
                cur_dot = ""
                cur_stone = ""
            
            if j == len(rows) -1:
                tilted_rows[i] = tilted_rows[i] + cur_dot + cur_stone

    return tilted_rows

def transpose(lst):
    trans = ["" for l in range(len(lst[0]))]
    for line in lst:
        for j, c in enumerate(line):
            trans[j] = trans[j] + c

    return trans

with open(f"2023/14/{sys.argv[1]}", "r") as file:
#with open(f"2023/14/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    pprint(lines)

    prev_rocks = [[]]
    rocks = lines
    rep_start = 0
    rep_diff = 0
    offset = 100
    for i in range(1000000000):
        n = transpose(north(transpose(rocks)))
        #pprint(n)
        w = west(n)
        #pprint(w)
        s = transpose(south(transpose(w)))
        #pprint(s)
        e = east(s)
        #pprint(e)
        if i > offset:
            if e in prev_rocks:
                for j, pr in enumerate(prev_rocks):
                    if pr == e:
                        rep_start = j + offset
                        rep_diff = i - j - offset
                break

            prev_rocks.append(e)

        rocks = e
    mod = (1000000000-rep_start) % rep_diff
    print("mod",mod)

    rocks = lines
    for i in range(rep_start+rep_diff+mod):
        n = transpose(north(transpose(rocks)))
        w = west(n)
        s = transpose(south(transpose(w)))
        e = east(s)

        rocks = e

    weight = 0
    for col in transpose(rocks):
        for i, c in enumerate(col):
            if c == "O":
                weight = weight + len(col) - i

    print(weight, file=sys.stderr)
