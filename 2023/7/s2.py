import sys
from pprint import pprint

cards = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
card_val = {"A": 14, "K": 13, "Q": 12, "T": 10, "9": 9, "8": 8, "7": 7, "6": 6, "5": 5, "4": 4, "3": 3, "2": 2, "J": 1}

hands = {"high": [], "one": [], "two": [],"three": [],"full": [],"four": [],"five": []}

with open(f"2023/7/{sys.argv[1]}", "r") as file:
    lines = [l.strip() for l in file.readlines()]

    for line in lines:
        line = line.split(" ")
        hand = line[0]
        bid = line[1]
        j_count = hand.count("J")

        print("h", hand, "b", bid, "j", j_count)

        unique_cards = list(set(list(hand)))
        print(unique_cards)
        if len(unique_cards) == 1:
            hands["five"].append((hand, bid))
            print("five")
        elif len(unique_cards) == 2:
            if j_count > 0:
                hands["five"].append((hand, bid))
            elif hand.count(unique_cards[0]) == 4 or hand.count(unique_cards[1]) == 4:
                hands["four"].append((hand, bid))
            else:
                hands["full"].append((hand, bid))
        elif len(unique_cards) == 3:
            if hand.count(unique_cards[0]) == 3 or hand.count(unique_cards[1]) == 3 or hand.count(unique_cards[2]) == 3:
                if j_count > 0:
                    hands["four"].append((hand, bid))
                else:
                    hands["three"].append((hand, bid))
            elif j_count == 2:
                hands["four"].append((hand, bid))
            elif j_count == 1:
                hands["full"].append((hand, bid))
            else:
                hands["two"].append((hand, bid))

        elif len(unique_cards) == 4:
            if j_count == 2:
                hands["three"].append((hand, bid))
            elif j_count == 1:
                hands["three"].append((hand, bid))
            else:
                hands["one"].append((hand, bid))
        else:
            if j_count > 0:
                hands["one"].append((hand, bid))
            else:
                hands["high"].append((hand, bid))

winnings = 0
rank = 1
for hand_type, hand_list in hands.items():
    if len(hand_list) > 0:
        hands_sorted = sorted(hand_list, key=lambda x: (card_val[x[0][0]], card_val[x[0][1]], card_val[x[0][2]], card_val[x[0][3]], card_val[x[0][4]]), reverse=False)
        for hand_bid_s in hands_sorted:
            winnings = winnings + int(hand_bid_s[1])*rank
            rank = rank + 1

print(winnings, file=sys.stderr)
