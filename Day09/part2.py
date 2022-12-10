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
    return ((self.x - coord2.x) ** 2) + ((self.y - coord2.y) ** 2) ** (1/2)
  
  def onSameAxis(self, other):
    return (self.x - other.x == 0) ^ (self.y - other.y == 0)
  
  def __hash__(self):
    return self.x ** (self.y ** 2)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __repr__(self):
    return '(' + str(self.x) + ', ' + str(self.y) + ')'

def main():
  rope = []

  for _ in range(0, ROPE_LENGTH):
    rope.append(Coord(0, 0))

  visited = set()
  visited.add(rope[-1])

  file = open('testInput.txt')

  for line in file:
    tokens = line.strip().split(' ')
    direction = tokens[0]
    numMoves = int(tokens[1])

    for _ in range(0, numMoves):
      print('\n')
      prevRope = []
      i = 0

      while i < ROPE_LENGTH:
        knot = rope[i]
        prevRope.append(knot.clone())

        if i > 0:
          prevKnotPosition = rope[i-1]
          distance = prevKnotPosition.distance(knot)

          needsMoved = distance > 2 or (distance == 2 and prevKnotPosition.onSameAxis(knot))
          print(knot, needsMoved)

          if not knot.onSameAxis(prevKnotPosition) and needsMoved:
            knotI = i
            knot.x = prevRope[i-1].x
            knot.y = prevRope[i-1].y
            xChange = knot.x - prevRope[i].x
            yChange = knot.y - prevRope[i].y

            print('head', knot)

            if i < ROPE_LENGTH - 1:
              i += 1
              while i < ROPE_LENGTH:
                current = rope[i]
                prevRope.append(current.clone())

                if current.onSameAxis(prevRope[knotI]) and current != prevRope[i-1]:
                  print('moving', current)
                  current.x += xChange
                  current.y += yChange
                else:
                  i -= 1
                  break

                i += 1

          else:
            prevKnot = rope[i-1]
            distance = prevKnot.distance(knot)

            if distance > 2 or (distance == 2 and prevKnot.onSameAxis(knot)):
              print('bumping', knot)
              knot.bump(direction)
        else:
          knot.bump(direction)
        
        if i == ROPE_LENGTH - 1:
          visited.add(rope[i])
        
        i += 1
        
      print(rope)

  file.close()
  print(len(visited))


if __name__ == "__main__":
  main()