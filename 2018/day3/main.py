from claim import Claim

def main() :
  claims = setupClaims('input.txt')
  #part1(claims) #takes two years :(
  part2(claims)


def part1(claims):
  totColPoints = []
  for i in range(len(claims)-1):
    claim = claims[i]

    for j in range(i+1,len(claims)):
      colPoints = claim.conflictPoints(claims[j])

      for p in colPoints:
        if p not in totColPoints:
          totColPoints.append(p)

  print(len(totColPoints))

def part2(claims):
  for c in claims:
    hasConflict = False
    for cComp in claims:
      if c.id != cComp.id and c.conflicts(cComp):
        hasConflict = True
        break

    if not hasConflict:
      print(c.toString())

def setupClaims(filename):
  claims = []

  with open(filename) as f:
    for line in f:
      sub = line.split(' ')

      idNbr = int(sub[0].split('#')[1])

      dim = sub[3].split('x')
      width = int(dim[0])
      height = int(dim[1])

      coord = sub[2].split(',')
      x = int(coord[0])
      y = int(coord[1][0:-1])

      c = Claim(idNbr, x,y,width,height)
      claims.append(c)

  return claims

if __name__ == '__main__':
  main()






