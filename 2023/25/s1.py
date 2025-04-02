import sys
from pprint import pprint
from collections import defaultdict 

def dfs(graph, start, end):
    fringe = [(start, [])]
    while fringe:
        state, path = fringe.pop()
        if path and state == end:
            yield path
            continue
        for next_state in graph[state]:
            if next_state in path:
                continue
            fringe.append((next_state, path+[next_state]))

#with open(f"2023/25/{sys.argv[1]}", "r") as file:
with open(f"2023/25/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    g = defaultdict(list)
    for line in lines:
        line = line.split(": ")
        key = line[0]
        val = line[1].split(" ")

        for v in val:
            g[key].append(v)
            g[v].append(key)
            g[v] = list(set(g[v]))

        g[key] = list(set(g[key]))

    cycles = [[node]+path for node in g for path in dfs(g, node, node)]
    print(list(set(cycles)))
    pprint(g)


#>>> graph = { 1: [2, 3, 5], 2: [1], 3: [1], 4: [2], 5: [2] }
#>>> 
#>>> len(cycles)
print(lines[-1], file=sys.stderr)
