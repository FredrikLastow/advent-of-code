import sys
from pprint import pprint

with open(f"2023/11/{sys.argv[1]}", "r") as file:
#with open(f"2023/11/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    stars = dict()

    for i, line in enumerate(lines):
        for j,c in enumerate(line):
            if c == "#":
                stars[(j,i)] = 0

    x_stars = set([s[0] for s in stars])
    y_stars = set([s[1] for s in stars])
    all_x = [x for x in range(len(lines[0]))]
    all_y = [x for x in range(len(lines))]

    missing_x = list()
    for i in range(len(lines[0])):
        if i not in x_stars:
            missing_x.append(i)

    missing_y = list()
    for i in range(len(lines)):
        if i not in y_stars:
            missing_y.append(i)

    adjusted_stars = dict()
    for star in stars.keys():
        x = star[0]
        y = star[1]

        new_x = x + sum([x > mx for mx in missing_x])
        new_y = y + sum([y > my for my in missing_y])

        adjusted_stars[(new_x, new_y)] = 0

    d = 0
    as_lst = list(adjusted_stars.keys())
    for i in range(len(as_lst)):
        s1 = as_lst[i]

        for j in range(i+1, len(as_lst)):
            s2 = as_lst[j]

            d = d + abs(s1[0]-s2[0]) + abs(s1[1]-s2[1])
            print(s1, s2, d)

    print(d)

    print("st", stars)
    print("mx", missing_x,"my", missing_y)



print(d, file=sys.stderr)
