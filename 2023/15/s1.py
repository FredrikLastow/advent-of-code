import sys
from pprint import pprint

with open(f"2023/15/{sys.argv[1]}", "r") as file:
#with open(f"2023/15/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]
    lines = lines[0].split(",")
    print(lines)

    values = []
    for line in lines:
        value = 0
        for c in line:
            a = ord(c)
            value = value + a
            value = value * 17
            value = value % 256

        print(value)
        values.append(value)

print(sum(values), file=sys.stderr)
