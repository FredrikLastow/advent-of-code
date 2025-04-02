import sys

with open(f"2023/3/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    x_len = len(lines[0])
    y_len = len(lines)
    coords = [(x, y) for x in range(-2, x_len+2) for y in range(-2, y_len+2)]
    val = [0 for x in range(len(coords))]
    gears = dict(zip(coords, val))
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == '*':
                gears[(i,j)] = 1


    gear_num = dict(zip(coords, [[] for x in range(len(coords))]))
    #print(symbols)

    for i in range(len(lines)):
        num = ""
        gears_toucing = []
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():
                if gears[(i-1,j-1)]:
                    gears_toucing.append((i-1,j-1))
                elif gears[(i-1,j)]:
                    gears_toucing.append((i-1,j))
                elif gears[(i-1,j+1)]:
                    gears_toucing.append((i-1,j+1))
                elif gears[(i,j-1)]:
                    gears_toucing.append((i,j-1))
                elif gears[(i,j+1)]:
                    gears_toucing.append((i,j+1))
                elif gears[(i+1,j-1)]:
                    gears_toucing.append((i+1,j-1))
                elif gears[(i+1,j)]:
                    gears_toucing.append((i+1,j))
                elif gears[(i+1,j+1)]:
                    gears_toucing.append((i+1,j+1))

                num = num + lines[i][j]

            elif num != "":
                for g in set(gears_toucing):
                    gear_num[g].append(int(num))

                num = ""
                gears_toucing = []

        if num != "":
            for g in gears_toucing:
                gear_num[g].append(int(num))

    ratio_sum = 0
    for k, v in gear_num.items():
        if len(v) == 2:
            ratio_sum += v[0]*v[1]

print(ratio_sum, file=sys.stderr)
