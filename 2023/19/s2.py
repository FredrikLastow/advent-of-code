import sys
from pprint import pprint

def rek(rating, rule, rules):

    if rule == "R":
        return [(rating, 0)]
    elif rule == "A":
        return [(rating, 1)]

    results = []
    cond = rules[rule]
    for attr, op, cval, res in cond:
        print("check", attr, op, cval, res)
        if attr == "end" and op == "end" and cval == -1:
            results = results + rek(rating, res, rules)
        else:
            if op == ">":
                rng = rating[attr]
                if rng[0] > cval:
                    results = results + rek(rating, res, rules)
                    break
                elif rng[1] > cval:
                    new_rat = rating.copy()
                    new_rat[attr] = (cval+1, rng[1])

                    results = results + rek(new_rat, res, rules)

                    rating[attr] = (rng[0], cval)

            elif op == "<":
                rng = rating[attr]
                if rng[1] < cval:
                    results = results + rek(rating, res, rules)
                    break
                elif rng[0] < cval:
                    new_rat = rating.copy()
                    new_rat[attr] = (rng[0], cval-1)

                    results = results + rek(new_rat, res, rules)

                    rating[attr] = (cval, rng[1])


    return results

with open(f"2023/19/{sys.argv[1]}", "r") as file:
#with open(f"2023/19/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    rules = dict()
    for line in lines:
        if line == "":
            break
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


    rat = dict({"x": (1,4000), "m": (1,4000), "a": (1,4000), "s": (1,4000)})
    res = rek(rat, "in", rules)
    pprint(res)

    s = 0
    for r, status in res:
        if status:
            add = 1
            for v in r.values():
                add = add * (v[1]+1-v[0])
            s = s + add
    
    print(s, file=sys.stderr)
