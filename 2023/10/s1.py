import sys
from pprint import pprint

pipes = list()
pipe_types = ["|", "-", "L", "J", "7", "F", ".", "S"]

def dfs(cur_coord, cur_p, prev_coord, step_count):
    if cur_p == "S":
        return step_count, True

    up = (cur_coord[0],cur_coord[1] - 1)
    right = (cur_coord[0]+1,cur_coord[1])
    down = (cur_coord[0],cur_coord[1] + 1)
    left = (cur_coord[0]-1,cur_coord[1])

    if cur_p in ["|", "L", "J", ""] and pipes[up] in ["7", "|", "F", "S"] and up != prev_coord:
        print("up", cur_coord, pipes[up])

        step_count, end = dfs(up, pipes[up], cur_coord, step_count + 1)
        if end:
            return step_count, end
    
    if cur_p in ["-", "L", "F", ""] and pipes[right] in ["J", "-", "7", "S"] and right != prev_coord:
        print("right", cur_coord, pipes[right])
        
        step_count, end = dfs(right, pipes[right], cur_coord, step_count + 1)

        if end:
            return step_count, end
    
    if cur_p in ["|", "7", "F", ""] and pipes[down] in ["J", "|", "L", "S"] and down != prev_coord:
        print("down", cur_coord, pipes[down])
        step_count, end = dfs(down, pipes[down], cur_coord, step_count + 1)

        if end:
            return step_count, end
    
    if cur_p in ["-", "J", "7", ""] and pipes[left] in ["L", "-", "F", "S"] and left != prev_coord:
        print("left", cur_coord, pipes[left])
        step_count, end = dfs(left, pipes[left], cur_coord, step_count + 1)

        if end:
            return step_count, end

    print("wrong path", cur_p, cur_coord)
    return step_count, False

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
        
        if cur_p in ["-", "L", "F", "S"] and pipes[right] in ["J", "-", "7", "S"] and right != prev_coord:
            print("right", p_c, pipes[right])
            next_pipes.append((p_c, right))
        
        if cur_p in ["|", "7", "F", "S"] and pipes[down] in ["J", "|", "L", "S"] and down != prev_coord:
            print("down", p_c, pipes[down])
            next_pipes.append((p_c, down))
        
        if cur_p in ["-", "J", "7", "S"] and pipes[left] in ["L", "-", "F", "S"] and left != prev_coord:
            print("left", p_c, pipes[left])
            next_pipes.append((p_c, left))

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

print(step_count)
print(int((step_count-1)/2), file=sys.stderr)
