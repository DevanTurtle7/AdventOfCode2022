ROPE_LENGTH = 10

class Coord:
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def clone(self):
    return Coord(self.x, self.y)
  
  def bump(self, direction):
    if direction == 'R':
      self.x += 1
    elif direction == 'L':
      self.x -= 1
    elif direction == 'U':
      self.y += 1
    elif direction == 'D':
      self.y -= 1

  def distance(self, coord2):
    diffX = abs(self.x - coord2.x)
    diffY = abs(self.y - coord2.y)

    if diffX == 1 and diffY == 1:
      return 1

    return ((diffX ** 2) + (diffY ** 2)) ** (1/2)
  
  def onSameAxis(self, other):
    return (self.x - other.x == 0) ^ (self.y - other.y == 0)
  
  def copy(self, coord):
    self.x = coord.x
    self.y = coord.y
  
  def diagFrom(self, coord):
    diffX = abs(self.x - coord.x)
    diffY = abs(self.y - coord.y)

    return diffX == 1 and diffY == 1
  
  def __hash__(self):
    return self.x ** (self.y ** 2)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __repr__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

def printGrid(rope):
  width = 26 
  height = 21
  xOffset = 11
  yOffset = 5
  #width = 6
  #height = 5
  #xOffset = 0
  #yOffset = 0
  grid = []

  for _ in range(0, height):
    row =[]
    for _ in range(0, width):
      row.append(None)
    grid.append(row)
  
  grid[height - (0 + yOffset + 1)][0 + xOffset] = 's'

  for i in range(len(rope) - 1, -1, -1):
    knot = rope[i]
    grid[height - (knot.y + yOffset + 1)][knot.x + xOffset] = i
  
  string = '\n\n\n'

  for row in grid:
    for item in row:
      if item == None:
        string += '.'
      elif item == 0:
        string += 'H'
      else:
        string += str(item)
    
    string += '\n'
  
  print(string)

def main():
  rope = []

  for _ in range(0, ROPE_LENGTH):
    rope.append(Coord(0, 0))

  visited = set()
  visited.add(rope[-1].clone())

  file = open('input.txt')

  for line in file:
    tokens = line.strip().split(' ')
    direction = tokens[0]
    numMoves = int(tokens[1])
    lastKnot = None
    lastKnotPrev = None

    for _ in range(0, numMoves):
      i = 0

      while i < ROPE_LENGTH:
        knot = rope[i]
        knotClone = knot.clone()

        if i == 0:
          knot.bump(direction)
        else:
          if knot.distance(lastKnot) > 1:
            if lastKnot.diagFrom(lastKnotPrev):
              if lastKnot.onSameAxis(knot):
                xDiff = lastKnot.x - knot.x
                yDiff = lastKnot.y - knot.y
                knot.x += (xDiff // 2)
                knot.y += (yDiff // 2)
              else:
                xDiff = lastKnot.x - lastKnotPrev.x
                yDiff = lastKnot.y - lastKnotPrev.y
                knot.x += xDiff
                knot.y += yDiff
            else:
              knot.copy(lastKnotPrev)
          #else:
            #print(i, 'other')
        
        i += 1
        lastKnot = knot 
        lastKnotPrev = knotClone

      visited.add(rope[ROPE_LENGTH-1].clone())
        
    #printGrid(rope)
      #print(rope)

  file.close()
  print(len(visited))
  #print(visited)


if __name__ == "__main__":
  main()