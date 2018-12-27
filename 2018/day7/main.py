instructions = {}
instructionsDep = {}

def setup():
  with open("input.txt") as f:
    for line in f:
      letter = line[5]
      dependLetter = line[36]

      if letter in instructions:
        instructions[letter].append(dependLetter)
      else:
        instructions[letter] = [dependLetter]

      if dependLetter in instructionsDep:
        instructionsDep[dependLetter].append(letter)
      else:
        instructionsDep[dependLetter] = [letter]

def main():
  startingInstr = []
  for key in instructions:
    dependent = False
    for item in instructions.values():
      if item.count(key) != 0:
        dependent = True
        break

    if not dependent:
      startingInstr.append(key)

  #part1(startingInstr)
  part2(startingInstr)

def part2(startingInstr):
  alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  availableInstr = sorted(startingInstr)
  instrOrder = ""
  time = -1
  workers = []

  while(True):
    time += 1

    newWorkers = []
    for i in range(len(workers)):
      w = workers[i]
      w["workTime"] += -1
      if w["workTime"] == 0:
        instr = w["instr"]
        instrOrder += instr

        if instr in instructions:
          newInstr = newInstructions(instr, instrOrder)
          availableInstr += newInstr
          availableInstr.sort()

      else:
        newWorkers.append(w)

    workers = newWorkers

    newAvailableInstr = []
    for instr in availableInstr:
      if len(workers) < 5:
        workTime = 60 + alphabet.index(instr) + 1
        workers.append({"instr": instr, "workTime": workTime})
      else:
        newAvailableInstr.append(instr)

    availableInstr = newAvailableInstr

    if len(workers) == 0:
      break;

  print(instrOrder, time) #971


def part1(startingInstr):
  availableInstr = sorted(startingInstr)
  instrOrder = ""

  while(len(availableInstr) > 0):
    nextInstr = availableInstr[0]
    instrOrde += nextInstr

    if nextInstr in instructions:
      newInstr = newInstructions(nextInstr, instrOrder)
      availableInstr += newInstr
      availableInstr.sort()

    availableInstr.remove(nextInstr)

  print(instrOrder) #CFMNLOAHRKPTWBJSYZVGUQXIDE

def newInstructions(instr, instrOrder):
  newInstrs = []
  instrs = instructions[instr]

  for instr in instrs:
    depInstr = instructionsDep[instr]

    unlocked = True
    for i in depInstr:
      if not i in instrOrder:
        unlocked = False
        break

    if unlocked:
      newInstrs.append(instr)

  return newInstrs

if __name__ == '__main__':
  setup()
  main()
