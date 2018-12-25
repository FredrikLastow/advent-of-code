def main():
  poly = ""
  with open('input.txt') as f:
    poly = f.read().splitlines()[0]

  #poly = "dabAcCaCBAcCcaDA"


  poly = collapsePoly(poly)

  # Part1
  #print(len(poly))

  part2(poly)


def part2(poly):
  letters = 'abcdefghijklmnopqrstuvwxyz'
  polyLen = len(poly)

  for c in letters:
    tempPoly = poly
    newPoly = tempPoly.replace(c, "")
    newPoly2 = newPoly.replace(c.upper(), "")
    tempLen = len(collapsePoly(newPoly2))

    if tempLen < polyLen:
      polyLen = tempLen

  print(polyLen)

def collapsePoly(poly):
  while(True):
    changed = False

    for i in range(len(poly) - 1):
      c1 = poly[i]
      c2 = poly[i + 1]

      if not c1.isupper() or not c2.isupper():
        if c1 == c2.upper() or c2 == c1.upper():
          changed = True
          poly = poly[:i] + poly[i+2:]
          break

    if not changed:
      break

  return poly

if __name__ == '__main__':
  main()
