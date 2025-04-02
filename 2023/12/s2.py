import sys
from pprint import pprint
import re
from itertools import product
from functools import cache

@cache
def count(springs, groups, cur_group):
    if len(springs) == 0:
        #print("end", springs, groups, cur_group, len(groups) > 0 and cur_group == groups[0] or not groups and not cur_group)
        return len(groups) == 1 and cur_group == groups[0] or not groups and not cur_group

    combs = 0

    s = ["#", "."] if springs[0] == '?' else springs[0]
    for p in s:
        #print(p, springs[1:], groups, cur_group)
        if p == '#':
            combs = combs + count(springs[1:], groups, cur_group+1)
        elif p == ".":
            if cur_group > 0:
                if len(groups) > 0 and cur_group == groups[0]:
                    combs = combs + count(springs[1:], groups[1:], 0)
                #else:
                    #print("group failed", cur_group, "expected", groups)
            else:
                combs = combs + count(springs[1:], groups, 0)

    return combs

with open(f"2023/12/{sys.argv[1]}", "r") as file:
#with open(f"2023/12/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    combs = 0
    for line in lines:
        line = line.split(" ")

        springs = '?'.join([line[0]]*5)
        groups = [int(g) for g in line[1].split(",")]*5
        print("start", springs, groups)

        c = count(springs, tuple(groups), 0)
        print(c)
        combs = combs + c

        

print(combs, file=sys.stderr)