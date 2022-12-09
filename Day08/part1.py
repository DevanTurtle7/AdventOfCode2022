
class Coord:
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def __hash__(self):
    return self.x ** self.y
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y


def getVisibleFromLine(line, reverse=False):
  visible = []

  if reverse:
    line = line[::-1]

  maxUntilNow = -1

  for i in range(0, len(line)):
    height = int(line[i])

    if height > maxUntilNow:
      if reverse:
        visible.append(len(line) - (i + 1))
      else:
        visible.append(i)
      maxUntilNow = height
  
  return visible


def main():
  file = open('/Users/dkavalchek/codingProjects/AdventOfCode2022/Day08/input.txt')
  visible = set()
  verticalLines = []
  y = 0

  for line in file:
    line = line.strip()
    
    for x in range(0, len(line)):
      height = line[x]

      if y == 0:
        verticalLines.append(height)
      else:
        verticalLines[x] = verticalLines[x] + height 

    for i in range(0, 2):
      visibleFromLine = getVisibleFromLine(line, i % 2 == 0) 
      for x in visibleFromLine:
        visible.add(Coord(x, y))

    y += 1

  for x in range(0, len(verticalLines)):
    line = verticalLines[x]

    for i in range(0, 2):
      visibleFromLine = getVisibleFromLine(line, i % 2 == 0) 
      for y in visibleFromLine:
        visible.add(Coord(x, y))
  
  file.close()
  print(len(visible))

if __name__ == '__main__':
  main()