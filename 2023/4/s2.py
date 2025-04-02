import sys

with open(f"2023/4/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    card_numbers = [x for x in range(1, len(lines)+1)]
    copies = dict(zip(card_numbers, [0 for x in range(1, len(lines)+1)]))
    for line in lines:
        card_number = int(line.split(":")[0].strip()[5:])
        copies_of_row = copies[card_number]
        
        line = line.split(":")[1].strip()

        winning = line.split("|")[0].strip().split(" ")
        numbers = line.split("|")[1].strip().split(" ")
        numbers = [i for i in numbers if i]

        winning_count = 0
        for n in numbers:
            if n in winning:
                winning_count += 1


        copied_rows = [x for x in range(card_number+1, card_number+winning_count+1)]
        for r in copied_rows:
            copies[r] += 1 + copies[card_number]
        print("card", card_number, "; ", line, "count", winning_count, "copies", copied_rows, "map", copies)

    total_scratch_cards = 0
    for v in copies.values():
        total_scratch_cards += v + 1

print(total_scratch_cards, file=sys.stderr)
