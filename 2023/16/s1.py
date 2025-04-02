import sys
from pprint import pprint

def solve(coords, history, start_c, start_d):

    hist = history
    c = start_c
    d = start_d
    new = []
    while True:
        print()
        print("c,d", (c[0],c[1],d[0],d[1]), coords[c])
        print("new", new)
        if (c[0],c[1],d[0],d[1]) in hist:
            print("cur in hist", (c[0],c[1],d[0],d[1]))
            return new, history
        else:
            hist.append((c[0], c[1], d[0], d[1]))

        next_c = (c[0]+d[0],c[1]+d[1])

        if next_c not in coords:
            print("next not in coord", next_c)
            return new, history

        con = coords[next_c]
        next_d = (0,0)
        if con == ".":
            next_d = d
        elif con == "/":
            if d[0] > 0:
                next_d = (0,-1)
            elif d[0] < 0:
                next_d = (0,1)
            elif d[1] > 0:
                next_d = (-1,0)
            elif d[1] < 0:
                next_d = (1,0)
        elif con == "\\":
            if d[0] > 0:
                next_d = (0,1)
            elif d[0] < 0:
                next_d = (0,-1)
            elif d[1] > 0:
                next_d = (1,0)
            elif d[1] < 0:
                next_d = (-1,0)
        elif con == "|":
            if d[0] != 0:
                new.append((next_c[0],next_c[1],0,1))
                next_d = (0,-1)
            else:
                next_d = d
        elif con == "-":
            if d[1] != 0:
                new.append((next_c[0],next_c[1],-1,0))
                next_d = (1,0)
            else:
                next_d = d

        c = next_c
        d = next_d
        
with open(f"2023/16/{sys.argv[1]}", "r") as file:
#with open(f"2023/16/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    coords = dict()
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            coords[(j,i)] = c

    new = [(0,0,0,1)]
    history = []
    while len(new) > 0:
        c = new.pop()
        print()
        print("starting",c)
        news, history = solve(coords, history, (c[0],c[1]), (c[2],c[3]))

        for n in news:
            new.append(n)
        new = list(set(new))
        print("new", news)
    print("h", history, len(set(history)))

    xyh = [(h[0], h[1]) for h in history]
    y = []
    for i, line in enumerate(lines):
        x = ""
        for j, c in enumerate(line):
            if (j,i) in xyh:
                x = x+"#"
            else:
                x = x+"."

        y.append(x)
    print(len(xyh), len(set(xyh)))

    pprint(y)

print(len(set(xyh)), file=sys.stderr)