from graphics import *

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

  ww = 2000
  wh = 1500
  win = GraphWin("Day 23", ww, wh)

  xMax = 200144301
  xMin = -170854721
  xDiff = xMax - xMin

  yMax = 171746322
  yMin = -120589179
  yDiff = yMax - yMin

  zMax = 192340365
  zMin = -154354348
  zDiff = zMax - zMin

  for bot in bots:
    z = bot[2]

    if z < zMin:
      zMin = z
    elif z > zMax:
      zMax = z

    print(zMin, zMax)


    circle = Circle(Point(bot[0]*ww/yDiff,bot[2]*wh/zDiff), 3)
    #print(bot[0]*xScale,bot[1]*yScale)
    circle.setFill("black")
    circle.draw(win)



  win.getMouse()

if __name__ == '__main__':
  main()


