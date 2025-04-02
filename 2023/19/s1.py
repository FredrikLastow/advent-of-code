import sys
from pprint import pprint

with open(f"2023/19/{sys.argv[1]}", "r") as file:
#with open(f"2023/19/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    rules = dict()
    ratings = list()
    rowsSwitch = False
    for line in lines:
        if line == "":
            rowsSwitch = True
        elif rowsSwitch:
            line = line[1:-1].split(",")
            rating = dict()
            for r in line:
                r = r.split("=")
                rating[r[0]] = int(r[1])

            ratings.append(rating)
        else:
            wf, rule = line.split("{")
            rule = rule[:-1].split(",")
            els = rule[-1]
            checks = list()
            for r in rule[:-1]:
                check, res = r.split(":")
                attr = check[0]
                op = check[1]
                val = int(check[2:])
                checks.append((attr,op,val,res))

            checks.append(("end", "end", -1, els))
            rules[wf] = checks
    pprint(rules)
    pprint(ratings)

    results = list()
    print()
    for rat in ratings:
        rule = "in"
        while True:
            print("rule", rule)
            if rule == "R":
                results.append((rat, 0))
                break
            elif rule == "A":
                results.append((rat, 1))
                break

            matched = False
            for attr, op, cval, res in rules[rule]:
                print("check", attr, op, cval, res)
                if attr == "end" and op == "end" and cval == -1:
                    rule = res
                    break
                else:
                    val = rat[attr]
                    if op == ">" and val > cval:
                        rule = res
                        break
                    elif op == "<" and val < cval:
                        rule = res
                        break
    pprint(results)
    s = 0
    for rat, status in results:
        if status:
            s = s + sum([x for x in rat.values()])
    
    print(s, file=sys.stderr)
