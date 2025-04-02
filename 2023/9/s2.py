import sys
from pprint import pprint


#with open(f"2023/9/test", "r") as file:
with open(f"2023/9/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    future_sum = 0
    for line in lines:
        history = [int(x) for x in line.split(" ")]

        diffs = [history]
        cur_diff = history
        while sum(cur_diff) != 0:
            cur_diff = [j-i for i, j in zip(cur_diff[:-1], cur_diff[1:])] 
            diffs.append(cur_diff)

        print(diffs)


        below = 0
        for diff in diffs[::-1]:
            right = diff[0]
            future = right - below

            print(diff, right, below, future)

            below = future

        future_sum = future_sum + below


print(future_sum, file=sys.stderr)
