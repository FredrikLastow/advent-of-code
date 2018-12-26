from patch import Patch

patches = []
usedPoints = []
duplicatePoints = []
limits = [40, 40, 340, 340]

def setup():
  with open("input.txt") as f:
    for line in f:
      coord = line.split(',')
      x = int(coord[0])
      y = int(coord[1].strip())

      patches.append(Patch(x, y))
      usedPoints.append([x,y])

def main():
  #part1()
  part2()

def part2():
  area = 0
  for x in range(380):
    for y in range(380):
      dist = 0
      for patch in patches:
        dx = abs(x - patch.xStart)
        dy = abs(y - patch.yStart)
        dist += dy + dx

      if dist < 10000:
        area += 1

  print(area)


# Takes six years
def part1():
  for i in range(200):
    expand()

    area = 0
    if i > 30:
      for patch in patches:
        patchArea = len(patch.area)

        if not patch.isOuter(limits) and patchArea > area:
          area = patchArea
    print(i, area)


def expand():
  newOuterPoints = []
  for patch in patches:
    expandPoints = patch.getExpandPoints()
    filteredPoints = filter(limit, expandPoints)

    patch.outerPoints.clear()

    for p in filteredPoints:
      patch.outerPoints.append(p)
      newOuterPoints.append(p)

  for patch in patches:
    for p in patch.outerPoints:
      if usedPoints.count(p) == 0:
        if newOuterPoints.count(p) > 1 and duplicatePoints.count(p) == 0:
          duplicatePoints.append(p)
          usedPoints.append(p)
        else:
          patch.area.append(p)
          usedPoints.append(p)


def limit(point):
  x = point[0]
  y = point[1]

  xmin = limits[0]
  xmax = limits[3]
  ymin = limits[1]
  ymax = limits[2]

  if x > xmin and x < xmax and y > ymin and y < ymax:
    return True
  else:
    return False

if __name__ == '__main__':
  setup()
  main()
