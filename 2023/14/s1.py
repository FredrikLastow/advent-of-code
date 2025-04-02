import sys
from pprint import pprint

with open(f"2023/14/{sys.argv[1]}", "r") as file:
#with open(f"2023/14/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    cols = ["" for l in range(len(lines[0]))]
    for line in lines:
        for j, c in enumerate(line):
            cols[j] = cols[j] + c

    print(cols)

    tilted_cols = ["" for l in range(len(lines[0]))]
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

    weight = 0
    for col in tilted_cols:
        for i, c in enumerate(col):
            if c == "O":
                weight = weight + len(col) - i
    print(tilted_cols)



    print(weight, file=sys.stderr)
