def main():
	elves = list([0])

	with open("input1.txt") as f:
		for line in f:
			if line == '\n':
				elves.append(0)
			else:
				cal = elves[len(elves) - 1]
				cal += int(line)
				elves[len(elves) - 1] = cal

	i = elves.index(max(elves))
	print(i,elves[i])

	elves = sorted(elves)
	print(sum(elves[-3:]))

if __name__ == '__main__':
	main()