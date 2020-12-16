def main():
	tree_map = []
	with open('input.txt') as f:
		for line in f:
			tree_map.append(line.strip())

	#part1(tree_map)
	part2(tree_map)

def part1(tree_map):
	print(count_trees(3,1, tree_map))

def part2(tree_map):
	slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

	prod = 1
	for slope in slopes:
		prod *= count_trees(slope[0], slope[1], tree_map)

	print(prod)

def count_trees(s_r, s_d, tree_map):
	n_trees = 0

	steps_d = 0
	steps_r = 0
	start_r = 0

	while steps_d*s_d <= len(tree_map) - 1:
		if start_r + steps_r*s_r >= len(tree_map[0]):
			start_r = (start_r + steps_r*s_r) % (len(tree_map[0]) - 1) - 1
			steps_r = 0

		n_trees += tree_map[steps_d*s_d][start_r + steps_r*s_r] == '#'

		steps_d += 1
		steps_r += 1

	return n_trees

if __name__ == '__main__':
	main()