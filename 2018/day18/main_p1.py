def main() :
  with open("input.txt") as f:
    acres = f.read().splitlines();

  columns = len(acres[0])
  rows = len(acres)
  changed = 0
  for t in range(5000):
    newAcres = []
    if changed == 0 and t > 0:
      print(t)
      break
    else:
      changed = 0

    for r in range(rows):
      newAcreLine = ""
      for c in range(columns):
        surround = surroundingAcres(acres, r, c)
        newAcre = changeAcre(acres[r][c], surround)

        if newAcre != acres[r][c]:
          changed += 1

        newAcreLine += newAcre

      newAcres.append(newAcreLine)
    acres = newAcres;

  wa = 0
  ly = 0
  for line in acres:
    wa += line.count('|')
    ly += line.count('#')

  print(wa*ly)

def surroundingAcres(acres, r, c):
  surroundingAcres = ""
  width = len(acres[0])
  height = len(acres)

  for i in range(-1,2):
    for j in range(-1,2):
      rs = r + i
      cs = c + j

      if rs < width and rs > -1 and cs < height and cs > -1:
        if rs != r or cs != c:
          surroundingAcres += acres[rs][cs]

  return surroundingAcres

def changeAcre(acre, surround):
  newAcre = ""
  if acre == "." and surround.count("|") > 2:
    newAcre = "|"
  elif acre == "|" and surround.count("#") > 2:
    newAcre = "#"
  elif acre == "#" :
    if surround.count("#") > 0 and surround.count("|") > 0:
      newAcre = "#"
    else:
      newAcre = "."
  else:
    newAcre = acre

  return newAcre

if __name__ == '__main__':
  main()


