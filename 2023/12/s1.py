import sys
from pprint import pprint
import re
from itertools import product

def generate_combinations(group):
    replacements = {'?': ['.', '#']}
    replacement_options = [replacements.get(c, [c]) for c in group]
    
    combinations = [''.join(p) for p in product(*replacement_options)]
    return combinations

#with open(f"2023/12/{sys.argv[1]}", "r") as file:
with open(f"2023/12/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    combs = 0
    for line in lines:
        line = line.split(" ")

        springs = line[0]
        groups = [int(g)*"#" for g in line[1].split(",")]

        sping_combs = generate_combinations(springs)
        sping_combs_f = []
        for c in sping_combs:
            c_groups = re.findall("[^.]+", c)
            if c_groups == groups:
                sping_combs_f.append(c)

        #print("comf", springs, sping_combs_f, len(sping_combs_f), groups)
        print(len(sping_combs_f))
        combs = combs + len(sping_combs_f)


print(combs, file=sys.stderr)
