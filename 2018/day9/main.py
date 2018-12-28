from marble import Marble

def main():
  '''
  Input
  428 players; last marble is worth 70825 points

  Examples
  9 players; last marble iw worth 25 points: high score is 32
  10 players; last marble is worth 1618 points: high score is 8317    X
  13 players; last marble is worth 7999 points: high score is 146373  X
  17 players; last marble is worth 1104 points: high score is 2764    X
  21 players; last marble is worth 6111 points: high score is 54718   X
  30 players; last marble is worth 5807 points: high score is 37305   X
  '''

  playerCount = 428
  finishMarbleScore = 70825*100

  playerScores = [0]*playerCount
  startMarble = Marble(0)
  firstMarble = Marble(1, startMarble, startMarble)
  startMarble.next = firstMarble
  startMarble.prev = firstMarble

  curMarbleVal = 1
  curMarble = firstMarble
  curPlayer = 0
  marbleCount = 2

  while (curMarbleVal < finishMarbleScore):
    curMarbleVal += 1
    print(curMarbleVal*100/finishMarbleScore)
    if curPlayer == playerCount - 1:
      curPlayer = 0
    else:
      curPlayer += 1

    if curMarbleVal % 23 == 0:
      score = curMarbleVal
      nextMarble = curMarble
      for n in range(7):
        nextMarble = nextMarble.prev

      score += nextMarble.value
      curMarble = nextMarble.next
      nextMarble.prev.next = nextMarble.next
      nextMarble.next.prev = nextMarble.prev
      playerScores[curPlayer] += score
    else:
      nextMarble = curMarble.next
      newMarble = Marble(curMarbleVal)
      nextMarble.addAfter(newMarble)
      curMarble = newMarble
      marbleCount += 1

  print("high score", max(playerScores)) #398502

if __name__ == '__main__':
  main()
