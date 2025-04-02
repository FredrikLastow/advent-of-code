import sys
from pprint import pprint

def findMirrored(lst):
    mirror = list()
    for i, line in enumerate(lst):

        if i < len(lst)-1 and line == lst[i+1]:
            mirror.append(i)

    return mirror

def evaluateMirrors(mirrors, lst):
    real_m = list()
    for m in mirrors:
        w = len(lst)
        steps = min(abs(w-(m+2)), m) 
        
        all_match = True
        for s in range(steps):
            if lst[m+2+s] != lst[m-s-1]:
                all_match = False

        if all_match:
            real_m.append(m)

    return real_m

def solve(p):
    score = 0
    cols = ["" for l in range(len(p[0]))]
    mirror_row = list()

    for i, line in enumerate(p):
        for j, c in enumerate(line):
            cols[j] = cols[j] + c

    mirror_row = findMirrored(p)
    rm = evaluateMirrors(mirror_row, p)
    if len(rm) > 0:
        score = (rm[0]+1)*100

    mirror_col = findMirrored(cols)
    cm = evaluateMirrors(mirror_col, cols)
    if len(cm) > 0:
        score = cm[0]+1

    return rm, cm


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

    score = 0
    for p in patterns:
        print()
        rm,cm = solve(p)

        found_smudge = False
        for i, line in enumerate(p):

            if found_smudge:
                break

            for j, c in enumerate(line):
                new_p = p.copy()
                if new_p[i][j] == ".":
                    new_p[i] = new_p[i][:j] + "#" + new_p[i][j+1:]
                else:
                    new_p[i] = new_p[i][:j] + "." + new_p[i][j+1:]

                nrm, ncm = solve(new_p)
                if len(nrm) > 0 and nrm != rm:
                    for x in nrm:
                        if x in rm:
                            nrm.remove(x)

                    pprint(p)
                    pprint(new_p)
                    print("coord", (i,j), "old", rm, cm, "new row", nrm, ncm)

                    rm = nrm
                    cm = []
                    found_smudge = True
                    break
                
                if len(ncm) > 0 and ncm != cm:
                    for x in ncm:
                        if x in cm:
                            ncm.remove(x)
                    pprint(p)
                    pprint(new_p)
                    print("coord", (i,j), "old", rm, cm, "new row", nrm, ncm)
                    cm = ncm
                    rm = []
                    found_smudge = True
                    break

        if len(rm) > 0:
            score = score + (rm[0]+1)*100

        if len(cm) > 0:
            score = score + cm[0]+1


print(score, file=sys.stderr)
