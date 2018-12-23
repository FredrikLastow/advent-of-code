def main() :
  bots = []

  with open("input.txt") as f:
    for line in f:
      coordStr = line[line.find('<')+1:line.find('>')]
      coords = list(map(int, coordStr.split(',')))
      radiusStr = line.split('=')[2].rstrip()
      coords.append(int(radiusStr))

      bots.append(coords)
      #bots.append([int(line[5:6]), int(line[7:8]), int(line[9:10]), int(line[15:16])])

  maxR = 0
  botMax = []
  for i in range(len(bots)):
    radius = bots[i][3]
    if radius > maxR:
      maxR = radius
      botMax = bots[i]

  bots.remove(botMax)

  rangeCount = 1
  for bot in bots:
    dx = abs(bot[0]-botMax[0])
    dy = abs(bot[1]-botMax[1])
    dz = abs(bot[2]-botMax[2])

    d = dx + dy + dz
    if (d <= maxR):
      rangeCount += 1

  print(rangeCount)

if __name__ == '__main__':
  main()


