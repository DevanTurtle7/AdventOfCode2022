
class Coord:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __hash__(self):
    return self.x ** self.y
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

def getReverseIndex(i, len):
  return len - (i + 1)

def getVisibleFromLine(line, reverse=False):
  visible = []

  if reverse:
    line = line[::-1]

  maxUntilNow = -1

  for i in range(0, len(line)):
    height = int(line[i])

    if height > maxUntilNow:
      if reverse:
        visible.append(getReverseIndex(i, len(line)))
      else:
        visible.append(i)
      maxUntilNow = height
  
  return visible


def getVisibilityScoreAlongAxis(line, index, reverse=True):
  count = 1
  houseHeight = int(line[index])
  blocked = False

  if reverse:
    index = getReverseIndex(index, len(line))
  
  while index + count < len(line) and not blocked:
    height = int(line[index])

    if height >= houseHeight:
      blocked = True 

    count += 1

  return count

def getVisibleFromLines(lines, reverseCoords=False):
  visible = []

  for x in range(0, len(lines)):
    line = lines[x]

    for i in range(0, 2):
      visibleFromLine = getVisibleFromLine(line, i % 2 == 0) 

      for y in visibleFromLine:
        if not reverseCoords:
          visible.append(Coord(x, y))
        else:
          visible.append(Coord(y, x))
  
  return visible

def main():
  file = open('/Users/dkavalchek/codingProjects/AdventOfCode2022/Day08/testInput.txt')
  visible = {}
  verticalLines = []
  horizontalLines = []
  y = 0

  for line in file:
    line = line.strip()
    horizontalLines.append(line)
    
    for x in range(0, len(line)):
      height = line[x]

      if y == 0:
        verticalLines.append(height)
      else:
        verticalLines[x] = verticalLines[x] + height 

    y += 1 

  coords = getVisibleFromLines(horizontalLines)
  coords.extend(getVisibleFromLines(verticalLines, True))

  for coord in coords:
    visible[coord] = True
  
  file.close()
  print(len(visible))

if __name__ == '__main__':
  main()