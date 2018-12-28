class Marble(object):
  def __init__(self, value, prevMarble=None, nextMarble=None):
    super(Marble, self).__init__()
    self.value = value
    self.prev = prevMarble
    self.next = nextMarble

  def addAfter(self, newMarble):
    self.next.prev = newMarble
    newMarble.next = self.next
    newMarble.prev = self
    self.next = newMarble

  def toString(self):
    return self.value
