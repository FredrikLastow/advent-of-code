from node import Node

numbers = []
def setup():
  with open("input.txt") as f:
    global numbers
    numbers = f.readlines()[0].strip().split(' ')

def main():
  i = 0
  while(i < len(numbers)):
    rootNode = Node(numbers[i], numbers[i + 1])
    i += 2
    i = loopChildNodes(rootNode, i)

  print('metadata sum', rootNode.getMetadataSum())
  print('root node value', rootNode.getNodeValue())

def loopChildNodes(node, numIndex):
  for n in range(node.childCount):
    childNode = Node(numbers[numIndex], numbers[numIndex + 1])
    node.children.append(childNode)
    numIndex += 2

    if childNode.childCount == 0:
      numIndex = addMetaData(childNode, numIndex)
    else:
      numIndex = loopChildNodes(childNode, numIndex)

  numIndex = addMetaData(node, numIndex)
  return numIndex

def addMetaData(node, numIndex):
  for m in range(node.metadataCount):
    node.metadata.append(int(numbers[numIndex]))
    numIndex += 1

  return numIndex

if __name__ == '__main__':
  setup()
  main()
