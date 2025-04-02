import sys

locs = list()
with open(f"2023/5/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    seeds = lines[0].split(":")[1].strip().split(" ")
    print(seeds)

    
    for seed in seeds:
        cur_value = int(seed)
        print("seed", seed)
        mapped = False
        for line in lines:
            if line != "" and line[0].isnumeric():
                split = line.split(" ")

                dest_start = int(split[0])
                source_start = int(split[1])
                length = int(split[2])
                #print("cur", cur_value, ";", dest_start, source_start, length)
                if source_start <= cur_value and cur_value <= source_start + length and not mapped:
                    cur_value = dest_start + cur_value - source_start
                    mapped = True
                    #print("new val", cur_value)
            else:
                #print(" ")
                mapped = False

        locs.append(cur_value)
        #print("loc", cur_value)
print(locs)
print(min(locs), file=sys.stderr)
