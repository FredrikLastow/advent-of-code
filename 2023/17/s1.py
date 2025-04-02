import sys
from pprint import pprint

def djik(source, dest, graph, dist):

    explored = []
    front = [source]
    i = 0
    while len(front) > 0:
        node = front.pop()
        x = node[0]
        y = node[1]
        v = node[2]
        vc = node[3]

        if v == 0:
            dist[(x,y)] = min(dist.get((x,y+1),0) + graph[(x,y)], dist[(x,y)])
        elif v == 1:
            dist[(x,y)] = min(dist.get((x-1,y),0) + graph[(x,y)], dist[(x,y)])
        elif v == 2:
            dist[(x,y)] = min(dist.get((x,y-1),0) + graph[(x,y)], dist[(x,y)])

        if graph.get((x,y-1)) and graph.get((x,y-1)) not in front and v != 2:
            if vc != 3 or v != 0:
                vcount = vc + 1 if v == 0 else 0
                front.append((x,y-1,0, vcount))

        if graph.get((x+1,y)) and graph.get((x+1,y)) not in front:
            if vc != 3 or v != 1:
                vcount = vc+1 if v == 1 else 0
                front.append((x+1,y,1,vcount))

        if graph.get((x,y+1)) and graph.get((x,y+1)) not in front and v != 0:
            if vc != 3 or v != 2:
                vcount = vc+1 if v == 2 else 0
                front.append((x,y+1,2,vcount))

        explored.append((x,y))
        i = i + 1
        if i == 10:
            break
        print("node", node, "front", front, "explored", explored)

    return dist
        



#with open(f"2023/17/{sys.argv[1]}", "r") as file:
with open(f"2023/17/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    grid = dict()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            grid[(j,i)] = int(c)

    pprint(grid)

    dist = dict(zip(grid.keys(), [100000000000 for k in grid.keys()]))
    pprint(dist)

    start = (0,0,1,0)
    grid[(0,0)] = 0
    dest = (len(lines[0])-1,len(lines)-1)
    dist = djik((0,0,1,0), dest, grid, dist)
    pprint(dist)

print(lines[-1], file=sys.stderr)
