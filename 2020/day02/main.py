def main():

  count_valid_n = 0
  pos_valid_n = 0

  with open('input.txt') as f:
    for line in f:
      policy, pwd = line.strip().split(": ")
      count_valid_n += count_valid(policy, pwd)
      pos_valid_n += pos_valid(policy, pwd)

  print(count_valid_n)
  print(pos_valid_n)

def count_valid(policy, pwd):
  min_count, max_count = list(map(int, policy[:-2].split('-')))
  c_count = pwd.count(policy[-1])
  
  return c_count <= max_count and c_count >= min_count
  
def pos_valid(policy, pwd):
  pos_a, pos_b = list(map(int, policy[:-2].split('-')))
  c = policy[-1]

  return (pwd[pos_a-1] == c) + (pwd[pos_b-1] == c) == 1

if __name__ == '__main__':
  main()
