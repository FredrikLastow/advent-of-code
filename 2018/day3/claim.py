class Claim(object):
  def __init__(self, idNbr, x, y, w, h):
    super(Claim, self).__init__()
    self.id = idNbr
    self.x = x
    self.y = y
    self.xe = x + w - 1
    self.ye = y + h - 1

  def conflicts(self, claim):
    xs = range(self.x,self.xe + 1)
    xc = range(claim.x, claim.xe + 1)

    ys = range(self.y,self.ye + 1)
    yc = range(claim.y, claim.ye + 1)

    xConflict = set(xs) & set(xc)
    yConflict = set(ys) & set(yc)

    hasConflict = False
    if xConflict and yConflict:
      hasConflict = True


    return hasConflict

  def conflictPoints(self, claim):
    points = []

    xs = range(self.x, self.xe + 1)
    xc = range(claim.x, claim.xe + 1)

    ys = range(self.y,self.ye + 1)
    yc = range(claim.y, claim.ye + 1)

    xConflict = set(xs) & set(xc)
    yConflict = set(ys) & set(yc)
    if xConflict and yConflict:
      for x in xConflict:
        for y in yConflict:
          points.append([x,y])

    return points

  def toString(self):
    return self.id, self.x, self.y, self.xe, self.ye
