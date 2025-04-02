import sys

engine_sum = 0

with open(f"2023/3/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    x_len = len(lines[0])
    y_len = len(lines)
    coords = [(x, y) for x in range(-2, x_len+2) for y in range(-2, y_len+2)]
    val = [0 for x in range(len(coords))]
    symbols = dict(zip(coords, val))
    
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] !=  '.' and not lines[i][j].isdigit():
                symbols[(i,j)] = 1

    #print(symbols)

    for i in range(len(lines)):
        num = ""
        has_symbol = False
        for j in range(len(lines[i])):
            if lines[i][j].isdigit():                
                s = symbols[(i-1,j-1)]+symbols[(i-1,j)]+symbols[(i-1,j+1)]+symbols[(i,j-1)]+symbols[(i,j+1)]+symbols[(i+1,j-1)]+symbols[(i+1,j)]+symbols[(i+1,j+1)]
                if s > 0:
                    has_symbol = True

                num = num + lines[i][j]

            elif num != "":
                if has_symbol:
                    engine_sum += int(num)

                num = ""
                has_symbol = False

        if num != "" and has_symbol:
            engine_sum += int(num)

print(engine_sum, file=sys.stderr)
