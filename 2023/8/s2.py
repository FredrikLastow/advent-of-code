import sys
import math

def finished(c_l):
    for c in c_l:
        if c[-1] != "Z":
            return False

    print("finished")
    return True

with open(f"2023/8/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    dirs = lines[0]
    starts = list()
    coords = dict()

    for line in lines[2:]:
        line = line.split(" = ")

        coord = line[0]
        turns = line[1].split(", ")

        left = turns[0][1:]
        right = turns[1][:-1]

        coords[coord] = (left, right)

        if coord[-1] == "A":
            starts.append(coord)

    print("start", starts)
    for s in starts:
        cur_c = s
        dir_i = 0
        turns = 0
        t_i = 0
        while True:
            d = dirs[dir_i]
            if d == "L":
                cur_c = coords[cur_c][0]
            elif d == "R":
                cur_c = coords[cur_c][1]
            
            turns = turns + 1

            if dir_i == len(dirs) - 1:
                dir_i = 0
            else:
                dir_i = dir_i + 1 

            if cur_c[-1] == 'Z':
                print(turns)
                turns = 0
                t_i = t_i +1

            if t_i == 10:
                break

lcm = math.lcm(11309, 19199, 12361, 16043, 13939, 18673, 18673)

print(lcm, file=sys.stderr)
