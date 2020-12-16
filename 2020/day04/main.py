import regex as re

def main():

	passports = list()
	passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']
	valid_count = 0

	with open('input.txt') as f:
		passport = dict()
		has_vaild_fields = True
		for line in f:
			if line == "\n":
				if has_vaild_fields:
					valid_count += check_passport_valid(passport, passport_fields)

				passports.append(passport)
				passport = dict()
				has_vaild_fields = True
			else:

				fields = line.strip().split(' ')
				for attr in fields:
					key, val = attr.split(':')
					passport[key] = val

					if not check_field_valid(key, val):
						has_vaild_fields = False

		if has_vaild_fields:
			valid_count += check_passport_valid(passport, passport_fields)

		passports.append(passport)

	print(valid_count)

def check_passport_valid(passport, passport_fields):
	field_count = len(passport.keys())

	return field_count == len(passport_fields) or field_count == len(passport_fields) - 1 and 'cid' not in passport.keys()

def check_field_valid(field, val):
	if field[-2:] == 'yr':
		val = int(val)

	if field == 'byr':
		return val >= 1920 and val <= 2002
	elif field == 'iyr':
		return val >= 2010 and val <= 2020
	elif field == 'eyr':
		return val >= 2020 and val <= 2030
	elif field == 'hgt':
		end = val[-2:]
	
		if end == 'cm':
			num = int(val[:-2])
			return num >= 150 and num <= 193
		elif end == 'in':
			num = int(val[:-2])
			return num >= 59 and num <= 76

		return False
	elif field == 'hcl':
		return val[0] == '#' and re.search('[0-9a-f]{6}', val[1:]) != None
	elif field == 'ecl':
		return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
	elif field == 'pid':
		return len(val) == 9

	return True

if __name__ == '__main__':
	main()