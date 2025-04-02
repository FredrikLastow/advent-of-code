import sys

def calc_ranges(lines):
    ranges = list()
    for line in lines:
        split = line.split(" ") 
        
        dest_start = int(split[0])
        source_start = int(split[1])
        length = int(split[2])

        ranges.append((source_start, source_start+length-1, dest_start, dest_start+length-1))

    return sorted(ranges, key=lambda x: x[0])

def apply(r, mapping):

    ms = []
    rl = r
    for i, (ss, se, ds, de) in enumerate(mapping):
        print("m", rl, ss, se, ds, de)
        if rl[0] < ss:
            ms.append((rl[0], ss-1))
            rl = (ss, rl[1])
            print("found pre", (r[0], ss-1), "new", rl)

        if rl[0] >= ss and rl[0] <= se:
            nrs = ds+rl[0]-ss
            nre = de+min(se, rl[1])-se
            ms.append((nrs,nre))
            print("found in, adding", (nrs,nre))
            if r[1] > se:
                print("new", (se+1, rl[1]))
                rl = (se+1, rl[1])
            else:
                break

        if i == len(mapping) - 1:
            ms.append(rl)

    print("mapped", ms)
    return ms

locs = list()
with open(f"2023/5/{sys.argv[1]}", "r") as file:
#with open(f"2023/5/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    sts = calc_ranges(lines[3:35])
    stf = calc_ranges(lines[37:72])
    ftw = calc_ranges(lines[74:101])
    wtl = calc_ranges(lines[103:120])
    ltt = calc_ranges(lines[122:164])
    tth = calc_ranges(lines[166:203])
    htl = calc_ranges(lines[205:244])

    #sts = calc_ranges(lines[3:5])
    #stf = calc_ranges(lines[7:10])
    #ftw = calc_ranges(lines[12:16])
    #wtl = calc_ranges(lines[18:20])
    #ltt = calc_ranges(lines[22:25])
    #tth = calc_ranges(lines[27:29])
    #htl = calc_ranges(lines[31:33])

    seeds = [int(x) for x in lines[0].split(": ")[1].split(" ")]
    seeds = [(seeds[i], seeds[i]+seeds[i+1]-1) for i in range(0, len(seeds), 2)]
    for s in seeds:
        print()
        print("seed", s, "sts", sts)
        soil = apply(s, sts)
        print("soil", soil)
        fert = list()
        for so in soil:
            fert = fert + apply(so, stf) 
        print("fert", fert)
        water = list()
        for f in fert:
            water = water + apply(f, ftw) 
        print("water", water)
        light = []
        for w in water:
            light = light + apply(w, wtl) 
        print("light", light)
        temp = []
        for l in light:
            temp = temp + apply(l, ltt)
        print("temp", temp)
        hum = []
        for  t in temp:
            hum = hum + apply(t, tth)
        print("hum", hum)
        loc = []
        for h in hum:
            loc = loc + apply(h, htl) 
        print("loc", sorted(loc, key=lambda x: x[0]))
        locs.append(sorted(loc, key=lambda x: x[0])[0][0])

print(min(locs), file=sys.stderr)



