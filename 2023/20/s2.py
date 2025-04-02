import sys
from pprint import pprint
from functools import cache

@cache
def handle(sig_val, source, dest, mod):
    if mod[0] == "%":
        if sig_val == 0:

            next_sval = 1 if not mod[1] else 0

            if not mod[1]:
                return (next_sval, ("%", True))
            else:
                return (next_sval, ("%", False))
        else:
            return (0,0)

    elif mod[0] == "&":

        new_def = list()
        for n, s in mod[1]:
            if n == source:
                new_def.append((n,sig_val))
            else:
                new_def.append((n,s))
        new_def = tuple(new_def)

        all_high = True
        for v in new_def:
            if v[1] == 0:
                all_high = False
                break
        print("&", all_high, new_def, mod)
        if all_high:
            return (0, new_def)
        else:
            return (1, new_def)

    elif mod[0] == "NO":
        return (sig_val, ("NO", 0))


#with open(f"2023/20/{sys.argv[1]}", "r") as file:
with open(f"2023/20/test", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    dest_modules = dict()
    input_modules = dict()
    modules = dict()
    all_m = list()
    for line in lines:
        mod, dest = line.split(" -> ")
        mod_type = mod[0]
        mod_name = mod[1:] if mod_type != "b" else "broadcaster"
        dest = dest.split(", ")

        all_m = all_m + dest

        dest_modules[mod_name] = dest

        for d in dest: 
            v = input_modules.get(d, [])
            v.append(mod_name)
            input_modules[d] = v

        if mod_type == "%":
            modules[mod_name] = ("%", False)
        elif mod_type == "&":
            modules[mod_name] = ("&", ())
        else:
            modules[mod_name] = ("NO", 0)

    for name, m in modules.items():
        if m[0] == "&":
            inp = input_modules[name]
            state = list()
            for m in inp:
                state.append((m,0))
            modules[name] = ("&", tuple(state))
    #modules["rx"] = ("NO", 0)
    modules["output"] = ("NO", 0)

    pprint(dest_modules)
    pprint(input_modules)
    print("MOD")
    pprint(modules)

    print(len(modules), len(set(all_m)))

    high_sig = 0
    low_sig = 0
    presses = 0
    found_rx = False
    for i in range(1):
        print(i)

        if found_rx:
            break
            
        signals = [(0, "", "broadcaster")]
        presses = presses + 1
        x = 0
        while len(signals) > 0:
            x = x + 1
            if x == 30:
                found_rx = True
                break

            print(signals)
            sig_val, source, dest = signals[0]
            signals = signals[1:]

            if dest == "rx" and sig_val == 0:
                print("FOUND")
                found_rx = True
                break
            
            print(sig_val, source, dest)
            if sig_val == 0:
                low_sig = low_sig + 1
            elif sig_val == 1:
                high_sig = high_sig + 1

            next_sval, new_def = handle(sig_val, source, dest, modules[dest])
            if (next_sval, new_def) != (0,0):
                #print("new")
                for d in dest_modules.get(dest, []):
                    signals.append((next_sval, dest, d))

                if len(new_def) > 0:
                    modules[dest] = (modules[dest][0], new_def)

            pprint(modules)

    print("high", high_sig, "low", low_sig, low_sig*high_sig)
    print(presses, file=sys.stderr)