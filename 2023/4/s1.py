import sys

total_points = 0

with open(f"2023/4/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    for line in lines:
        line = line.split(":")[1].strip()
        print(line)

        winning = line.split("|")[0].strip().split(" ")
        numbers = line.split("|")[1].strip().split(" ")
        numbers = [i for i in numbers if i]

        print(line.split("|")[1].strip())
        print(winning, numbers)
        points = 0
        for n in numbers:
            print(n)
            if n in winning:
                if points == 0:
                    points = 1
                else:
                    points = points*2

                print("winning", n, points)

        total_points = total_points + points


print(total_points, file=sys.stderr)
