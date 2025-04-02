import sys
from pprint import pprint

def findMirrored(lst):
    mirror = list()
    for i, line in enumerate(lst):

        if i < len(lst)-1 and line == lst[i+1]:
            mirror.append(i)

    return mirror

def evaluateMirrors(mirrors, lst):
    print(lst)
    real_m = list()
    for m in mirrors:
        print("m", m, lst[m], lst[m+1])
        w = len(lst)
        steps = min(abs(w-(m+2)), m) 

        print("len", m, w, abs(w-(m+3)), steps)
        
        all_match = True
        for s in range(steps):
            print("match",lst[m+1+s], lst[m-s] )
            if lst[m+2+s] != lst[m-s-1]:
                all_match = False

        if all_match:
            print("matched", m)
            real_m.append(m)
        else:
            print("notmatched")

    return real_m


with open(f"2023/13/{sys.argv[1]}", "r") as file:
#with open(f"2023/13/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    patterns = list()
    cur_p = []
    for line in lines:
        if line == "":
            patterns.append(cur_p)
            cur_p = []
        else:
            cur_p.append(line)
    patterns.append(cur_p)

    print("pat", patterns)

    score = 0
    for p in patterns:
        print()
        print("p", p)

        cols = ["" for l in range(len(p[0]))]
        mirror_row = list()


        for i, line in enumerate(p):

            if i < len(p)-1 and line == p[i+1]:
                mirror_row.append(i)

            for j, c in enumerate(line):
                cols[j] = cols[j] + c

        print("c", cols)

        mirror_col = findMirrored(cols)

        print(mirror_row, mirror_col)
        print("row")
        rm = evaluateMirrors(mirror_row, p)
        if len(rm) > 0:
            print("SCORE ROW", rm[0]*100)
            score = score + (rm[0]+1)*100

        print("col")
        cm = evaluateMirrors(mirror_col, cols)
        if len(cm) > 0:
            print("SCORE COL", cm[0]+1)
            score = score + cm[0]+1


print(score, file=sys.stderr)
