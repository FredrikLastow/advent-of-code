import sys

with open(f"2023/2/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    power_sum = 0

    for line in lines:
        power = 1
        min_bag = {"red": 0, "green": 0, "blue": 0}

        line = line.split(":")
        g_id = line[0][4:].strip()
        
        print(g_id, line)

        sets = line[1].split(";")
        for s in sets:
            cubes = s.strip().split(",")

            for c in cubes:
                split = c.strip().split(" ")
                n = split[0]
                col = split[1]

                if min_bag[col] < int(n):
                    min_bag[col] = int(n)

                print(g_id, n, col, min_bag)

        for v in min_bag.values():
            power = power * v

        power_sum = power_sum + power

print(power_sum, file=sys.stderr)

