import sys

with open(f"2023/2/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    possible_games = 0

    for line in lines:
        bag = {"red": 12, "green": 13, "blue": 14}
        print(line)

        line = line.split(":")
        g_id = line[0][4:].strip()
        print(g_id, bag)
        
        possible = True
        sets = line[1].split(";")
        for s in sets:
            cubes = s.strip().split(",")

            for c in cubes:
                split = c.strip().split(" ")
                n = split[0]
                col = split[1]

                if bag[col] < int(n):
                    possible = False
                    print(g_id, n, col)

        print(possible)
        if possible:
            possible_games += int(g_id)
        print(possible_games)

print(possible_games, file=sys.stderr)

