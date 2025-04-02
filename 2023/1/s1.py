import sys, os

cal_sum = 0

with open(f"2023/1/{sys.argv[1]}", "r") as file:
    for line in file:
        c_number = ""
        for c in line.strip():
            if c.isnumeric():
                c_number += c
                break

        for c in line.strip()[::-1]:
            if c.isnumeric():
                c_number += c
                break

        cal_sum += int(c_number)

print(cal_sum, file=sys.stderr)
