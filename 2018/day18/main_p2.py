from graphics import *

def main() :
  #win = GraphWin("Hej", 2000, 1500)

  with open("input2.txt") as f:
    acres = f.read().splitlines();


  columns = len(acres[0])
  rows = len(acres)
  ly = 0
  tree = 0
  result = []
  time = []
  tot = 0
  maxValue = 0
  for t in range(1,2000):
    ly = 0
    tree = 0
    newAcres = []

    for r in range(rows):
      newAcreLine = ""
      for c in range(columns):
        surround = surroundingAcres(acres, r, c)
        newAcre = changeAcre(acres[r][c], surround)

        newAcreLine += newAcre

      newAcres.append(newAcreLine)

    acres = newAcres;

    for line in acres:
      ly += line.count('#')
      tree += line.count('|')

    tot = ly*tree
    result.append(tot)

    if t == 26+1506:
      print(tot)
      break

  ts = 1506
  te = 1000000000
  tp = 26 #(te-ts)%28


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


