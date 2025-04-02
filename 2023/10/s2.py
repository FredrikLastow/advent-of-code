import sys
from pprint import pprint

import matplotlib.pyplot as plt
import numpy as np

pipes = dict()
loop = list()

def bfs(pipe_cs):
    next_pipes  = list()

    for prev_coord, p_c in pipe_cs:
        
        cur_p = pipes[p_c]
        up = (p_c[0],p_c[1] - 1)
        right = (p_c[0]+1,p_c[1])
        down = (p_c[0],p_c[1] + 1)
        left = (p_c[0]-1,p_c[1])

        print("prev", prev_coord, "cur", p_c, "cur p", cur_p, ";", up, right, down, left)

        if cur_p == "S" and prev_coord != p_c:
            return list(), True

        if cur_p in ["|", "L", "J", "S"] and pipes[up] in ["7", "|", "F", "S"] and up != prev_coord:
            print("up", p_c, pipes[up])
            next_pipes.append((p_c, up))
            loop.append(up)
        
        if cur_p in ["-", "L", "F", "S"] and pipes[right] in ["J", "-", "7", "S"] and right != prev_coord:
            print("right", p_c, pipes[right])
            next_pipes.append((p_c, right))
            loop.append(right)
        
        if cur_p in ["|", "7", "F", "S"] and pipes[down] in ["J", "|", "L", "S"] and down != prev_coord:
            print("down", p_c, pipes[down])
            next_pipes.append((p_c, down))
            loop.append(down)
        
        if cur_p in ["-", "J", "7", "S"] and pipes[left] in ["L", "-", "F", "S"] and left != prev_coord:
            print("left", p_c, pipes[left])
            next_pipes.append((p_c, left))
            loop.append(left)

    print("next", next_pipes)

    return next_pipes, False

with open(f"2023/10/{sys.argv[1]}", "r") as file:
#with open(f"2023/10/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    x_len = len(lines[0])
    y_len = len(lines)
    coords = [(x, y) for y in range(-1, y_len+1) for x in range(-1, x_len+1)]
    val = ["." for x in range(len(coords))]
    pipes = dict(zip(coords, val))

    start = (0,0)
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "S":
                start = (x,y)

            pipes[(x,y)] = lines[y][x]
    print(pipes, start)

    #step_count, end = dfs(start, "", start, 0)
    pipe_cs = [(start, start)]
    step_count = 0
    end = False
    while not end:

        pipe_cs, end = bfs(pipe_cs)
        step_count = step_count + 1
        print()
        print(end)

    loop = set(loop)
    loop_ins = list()

    pipe_types = ["|", "-", "L", "J", "7", "F", ".", "S"]
    sorted_loop = sorted(loop, key=lambda x: (x[0], x[1]), reverse=False)
    for y in range(len(lines)):

        inside = False
        inside_c = list()
        prev_pipe = ""
        for x in range(len(lines[y])):
            if (x,y) in loop:
                pipe = pipes[(x,y)]
                if pipe is not "-" and not (prev_pipe == "L" and pipe == "7") and not (prev_pipe == "F" and pipe == "J") :

                    if inside and len(inside_c) > 0:
                        loop_ins = loop_ins + inside_c
                        inside_c = list()

                    inside = not inside

                print((x,y), "edge", pipes[(x,y)], inside, len(inside_c))

            elif inside:
                print((x,y), "inside", pipes[(x,y)], inside)
                inside_c.append((x,y))
            else:
                print((x,y), "nothing", pipes[(x,y)], inside)

            if pipes[(x,y)] not in ["-", "."]:
                prev_pipe = pipes[(x,y)]

print(len(loop_ins), file=sys.stderr)
