class Node(object):
  """docstring for Node"""
  def __init__(self, childCount, metadataCount):
    super(Node, self).__init__()
    self.childCount = int(childCount)
    self.children = []
    self.metadataCount = int(metadataCount)
    self.metadata = []


  def getMetadataSum(self):
    metadataSum = 0

    for metadata in self.metadata:
      metadataSum += metadata

    for child in self.children:
      metadataSum += child.getMetadataSum()

    return metadataSum

  def getNodeValue(self):
    value = 0
    if self.childCount == 0:
      for metadata in self.metadata:
        value += metadata
    else:
      for metadata in self.metadata:
        if metadata <= self.childCount and not metadata == 0:
          value += self.children[metadata - 1].getNodeValue()

    return value

  def toString(self):
    return self.childCount, self.metadataCount

