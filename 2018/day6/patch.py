class Patch(object):
  def __init__(self, xStart, yStart):
    super(Patch, self).__init__()
    self.xStart = xStart
    self.yStart = yStart
    self.outerPoints = [[xStart, yStart]]
    self.d = 0
    self.area = [[xStart, yStart]]

  def getExpandPoints(self):
    self.d += 1

    newOuterPoints = []
    for point in self.outerPoints:
      x = point[0]
      y = point[1]

      dx = abs(x - self.xStart)
      dy = abs(y - self.yStart)

      coords = [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]

      for c in coords:
        if abs(c[0]-self.xStart) >= dx and abs(c[1]-self.yStart) >= dy and newOuterPoints.count(c) == 0:
          newOuterPoints.append(c)

    return newOuterPoints

  def isOuter(self, limits):
    xmin = limits[0]
    xmax = limits[3]
    ymin = limits[1]
    ymax = limits[2]


    for p in self.area:
      x = p[0]
      y = p[1]

      if abs(x - xmin) == 1 or abs(x - xmax) == 1 or abs(y - ymin) == 1 or abs(y - ymax) == 1:
        return True

    return False




