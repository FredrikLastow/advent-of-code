import sys
from pprint import pprint

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
            modules[mod_name] = ("&", {})
        else:
            modules[mod_name] = ("NO", 0)

    for name, m in modules.items():
        if m[0] == "&":
            inp = input_modules[name]
            state = dict()
            for m in inp:
                state[m] = 0
            modules[name] = ("&", state)
    #modules["rx"] = ("NO", 0)
    modules["output"] = ("NO", 0)

    pprint(dest_modules)
    pprint(input_modules)
    print("MOD")
    pprint(modules)

    print(len(modules), len(set(all_m)))

    high_sig = 0
    low_sig = 0
    for i in range(1000):

        signals = [(0, "", "broadcaster")]

        while len(signals) > 0:
            sig_val, source, dest = signals[0]
            signals = signals[1:]
            
            #print("sv", sig_val, "source", source, "dest", dest)
            if sig_val == 0:
                low_sig = low_sig + 1
            elif sig_val == 1:
                high_sig = high_sig + 1

            mod = modules[dest]
            if mod[0] == "%":
                if sig_val == 0:

                    next_sval = 1 if not mod[1] else 0

                    if not mod[1]:
                        modules[dest] = ("%", True)
                    else:
                        modules[dest] = ("%", False)

                    for d in dest_modules.get(dest, []):
                        signals.append((next_sval, dest, d))

            elif mod[0] == "&":

                mod[1][source] = sig_val
                all_high = True
                for k,v in mod[1].items():
                    if v == 0:
                        all_high = False
                        break

                if all_high:
                    for d in dest_modules.get(dest, []):
                        signals.append((0, dest, d))
                else:
                    for d in dest_modules.get(dest, []):
                        signals.append((1, dest, d))

            elif mod[0] == "NO":
                for d in dest_modules.get(dest, []):
                    signals.append((sig_val, dest, d))



    print("high", high_sig, "low", low_sig)
    print(high_sig*low_sig, file=sys.stderr)
