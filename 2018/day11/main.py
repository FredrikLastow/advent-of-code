def main():
  gsn = 9445
  powerGrid = createPowerGrid(gsn)

  maxPower = 0
  coords = []
  for l in range(1,30): # Part1: l = 3
    print(l)
    for r in range(len(powerGrid) - l):
      row = powerGrid[r]
      for c in range(len(row) - l):
        squareSum = 0
        for i in range(l):
          for j in range(l):
            squareSum += powerGrid[r + i][c + j]

        if squareSum > maxPower:
          maxPower = squareSum
          coords = [c + 1, r + 1, l]


  print(coords, maxPower)

def createPowerGrid(gsn):
  powerGrid = []
  for y in range(1,301):
    row = []
    for x in range(1,301):
      rackID = x + 10
      powerLevel = rackID * y
      powerLevel += gsn
      powerLevel = powerLevel * rackID
      powerLevel = str(powerLevel)[-3]
      powerLevel = int(powerLevel) - 5
      row.append(powerLevel)

    powerGrid.append(row)

  return powerGrid

if __name__ == "__main__":
  main()
