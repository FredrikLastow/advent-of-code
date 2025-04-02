import sys

with open(f"2023/6/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    times = [int(i) for i in lines[0][5:].split(" ") if i]
    dists = [int(i) for i in lines[1][9:].split(" ") if i]

    solves = []
    for i in range(len(times)):
        time = times[i]
        dist = dists[i]

        min_speed = int(dist/time)+1

        time_after_acc = time-min_speed
        print(time, dist, min_speed, min_speed*time, time_after_acc)

        n = 0
        for t in range(0, time_after_acc):
            v = min_speed + t
            time_remaing = time - v
            print(v, time_remaing, time_remaing*v)
            if time_remaing*v > dist:
                n = n + 1
        solves.append(n)
       

print("s", solves)
multi_sum = 1
for s in solves:
    multi_sum = multi_sum * s

print(multi_sum, file=sys.stderr)
