import sys

cal_sum = 0
number_str = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}

with open(f"2023/1/{sys.argv[1]}", "r") as file:
    for line in file:
        print(line)
        c_number = ""

        c_number_str = ""
        for c in line.strip():
            if c.isnumeric():
                c_number += c
                break

            c_number_str += c
            str_found = False
            for ns in number_str.keys():
                if ns in c_number_str:
                    c_number += str(number_str[ns])
                    str_found = True
                    break
            
            print(c, c_number, c_number_str)
            if str_found:
                break

        print(c, c_number, c_number_str)
        c_number_str = ""
        for c in line.strip()[::-1]:
            if c.isnumeric():
                c_number += c
                break

            c_number_str = c + c_number_str
            str_found = False
            for ns in number_str.keys():
                if ns in c_number_str:
                    c_number += str(number_str[ns])
                    str_found = True
                    break

            print(c, c_number, c_number_str)
            if str_found:
                break

        cal_sum += int(c_number)

print(cal_sum, file=sys.stderr)

