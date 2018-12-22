from graphics import *
import math

def main() :
  positions = []
  velocities = []
  win = GraphWin("Hej", 2000, 1500)
  win.setBackground("black")

  with open("input.txt") as f:
    for line in f:
      xPos = int(line[10:16])
      yPos = int(line[17:24])
      positions.append([xPos,yPos])

      xVel = int(line[36:38])
      yVel = int(line[39:42])
      velocities.append([xVel,yVel])

  for t in range(1,10392):
    for i in range(0,len(positions)):
      positions[i][0] += velocities[i][0]
      positions[i][1] += velocities[i][1]

      if (t > 10360 and t % 1 == 0):
        circle = Circle(Point(positions[i][0]*10-1000,positions[i][1]*10-700), 2)
        circle.setFill("white")
        circle.draw(win)
        #x = round((positions[i][0]+525000)*0.0182)
        #y = round((positions[i][1]+55000)*0.0136)

        #x = round((positions[i][0]+2000)*0.5)
        #y = round((positions[i][1]+2000)*0.375)

  for i in range(0,len(positions)):
    circle = Circle(Point(positions[i][0]*10-1000,positions[i][1]*10-700), 3)
    circle.setFill("red")
    circle.draw(win)

  win.getMouse()


if __name__ == '__main__':
  main()


