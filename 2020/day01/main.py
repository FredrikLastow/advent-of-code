def main():  
  expenses = list()
  with open('input.txt') as f:
    for line in f:
      expenses.append(int(line.strip()))

  print(part1(expenses))

  print(part2(expenses))


def part1(expenses):
  for i in range(len(expenses)-1):
    for j in range(i+1, len(expenses)):
      if expenses[i] + expenses[j] == 2020:
        return expenses[i]*expenses[j]

def part2(expenses):
  for i in range(len(expenses)-2):
    for j in range(i+1, len(expenses)-1):
      for k in range(j+1, len(expenses)):
        if expenses[i] + expenses[j] + expenses[k] == 2020:
          return expenses[i]*expenses[j]*expenses[k]



if __name__ == '__main__':
  main()
