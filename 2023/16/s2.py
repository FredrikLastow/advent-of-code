import sys
from pprint import pprint
from tqdm import tqdm

def solve(coords, history, start_c, start_d):

    hist = history
    c = start_c
    d = start_d
    new = []
    while True:
        if (c[0],c[1],d[0],d[1]) in hist:
            return new, history
        else:
            hist.append((c[0], c[1], d[0], d[1]))

        next_c = (c[0]+d[0],c[1]+d[1])

        if next_c not in coords:
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
    starts = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            coords[(j,i)] = c
            if i == 0:
                starts.append((j,-1,0,1))

            if i == len(lines)-1:
                starts.append((j, len(lines),0,-1))

            if j == 0:
                starts.append((-1,i,1,0))

            if j == len(line)-1:
                starts.append((len(line),i,-1,0))

    ens = dict()
    for s in tqdm(starts):
        new = [s]
        history = []
        while len(new) > 0:
            c = new.pop()
            news, history = solve(coords, history, (c[0],c[1]), (c[2],c[3]))

            for n in news:
                new.append(n)
            new = list(set(new))

        xyh = [(h[0], h[1]) for h in history]
        en = 0
        y = []
        for i, line in enumerate(lines):
            x = ""
            for j, c in enumerate(line):
                if (j,i) in xyh:
                    x = x+"#"
                    en = en + 1
                else:
                    x = x+"."

            y.append(x)
        ens[s] = len(set(xyh))-1

    max_k = (0,0)
    max_v = 0
    for k,v in ens.items():
        if v > max_v:
            max_k = k
            max_v = v
    print(max_k)
print(max_v, file=sys.stderr)
