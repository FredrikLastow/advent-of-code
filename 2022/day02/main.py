def main2():
	score = 0

	with open("input1.txt") as f:
		for line in f:
			rps_round = line.strip().split(" ")
			hand = rps_round[0]
			outcome = rps_round[1]

			score += calc_points(hand, outcome)
	print(score)

def main():
	score = 0

	with open("input1.txt") as f:
		for line in f:
			rps_round = line.strip().split(" ")
			hand = map_to_xyz(rps_round[0])
			response = rps_round[1]

			win_p = win(hand, response)
			hand_points = point(response)
			print(hand, response, win_p, hand_points)
			score += win_p + hand_points

	print(score)

def calc_points(hand, outcome):
	if outcome == 'X':
		if hand == 'A':
			return point('Z')
		elif hand == 'B':
			return point('X')
		elif hand == 'C':
			return point('Y')

	elif outcome == 'Y':
		return point(map_to_xyz(hand)) + 3
	elif outcome == 'Z':
		points = 6

		if hand == 'A':
			points += point('Y')
		elif hand == 'B':
			points += point('Z')
		elif hand == 'C':
			points += point('X')

		return points

def win(hand, response):
	if hand == response:
		return 3
	if (hand == 'X' and response == 'Y') or (hand == 'Y' and response == 'Z') or (hand == 'Z' and response == 'X'):
		return 6
	else:
		return 0

def map_to_xyz(hand):
	if hand == 'A':
		return 'X'
	elif hand == 'B':
		return 'Y'
	elif hand == 'C':
		return 'Z'


def point(response):
	if response == 'X':
		return 1
	elif response == 'Y':
		return 2
	elif response == 'Z':
		return 3


if __name__ == '__main__':
	main2()