import sys

with open(f"2023/6/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    times = [i for i in lines[0][5:].split(" ") if i]
    dists = [i for i in lines[1][9:].split(" ") if i]
    time = int(''.join(times))
    dist = int(''.join(dists))

    min_speed = int(dist/time)+1

    time_after_acc = time-min_speed

    n = 0
    for t in range(0, time_after_acc):
        v = min_speed + t
        time_remaing = time - v
        if time_remaing*v > dist:
            n = n + 1

print(n, file=sys.stderr)
