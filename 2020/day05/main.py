
def main():
	seat_ids = list()
	with open("input.txt") as f:
		for line in f:
			seat = line.strip()

			r_rng = [0, 127]
			c_rng = [0, 7]

			r = get_final_idx(r_rng, seat[:7], 'B', 'F')
			c = get_final_idx(c_rng, seat[7:], 'R', 'L')
		
			seat_ids.append(r*8+c)
	print("max seat id:", max(seat_ids))
	seat_ids = sorted(seat_ids)
	seat_rng = list(range(min(seat_ids), max(seat_ids) + 1))

	for i in range(len(seat_ids)):
		if seat_ids[i] != seat_rng[i]:
			print("seat id:", seat_rng[i])
			break

def get_final_idx(idx_range, seq, uph_c, loh_c):
	for char in seq:
		diff = round(abs(idx_range[1] - idx_range[0])/2)

		if char == uph_c:
			if diff == 0: 
				return idx_range[1]
			else:
				idx_range[0] += diff
		elif char == loh_c:
			if diff == 0: 
				return idx_range[0]
			else:
				idx_range[1] -= diff

if __name__ == '__main__':
	main()