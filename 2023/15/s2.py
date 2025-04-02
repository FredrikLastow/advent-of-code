import sys
from pprint import pprint

def hash(str):
    value = 0
    for c in str:
        a = ord(c)
        value = value + a
        value = value * 17
        value = value % 256

    return value

with open(f"2023/15/{sys.argv[1]}", "r") as file:
#with open(f"2023/15/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]
    lines = lines[0].split(",")
    print(lines)

    key = [x for x in range(256)]
    val = [[] for x in range(256)]
    boxes = dict(zip(key, val))

    print(boxes)
    for line in lines:
        if "=" in line:
            line = line.split("=")
            lab = line[0]
            fl = line[1]
            box = hash(lab)

            found = False
            for l, f in boxes[box]:
                if l == lab:
                    cl = boxes[box]
                    cl[cl.index((l,f))] = (l, fl)
                    found = True
                    break

            if not found:
                boxes[box].append((lab,fl))
            print(line, box, lab, fl)

        elif "-" in line:
            lab = line[:-1]
            box = hash(lab)

            for l, f in boxes[box]:
                if l == lab:
                    boxes[box].remove((l,f))
            print(line, box, lab)

    s = 0
    for k, v in boxes.items():
        if len(v) == 0:
            continue

        for i, (lab, fl) in enumerate(v):
            s = s + (k + 1) * (i + 1) * int(fl)
            print(i, lab, fl, s)


print(s, file=sys.stderr)
