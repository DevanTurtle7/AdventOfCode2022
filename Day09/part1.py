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
    return self.x - other.x == 0 or self.y - other.y == 0
  
  def __hash__(self):
    return self.x ** (self.y ** 2)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

def main():
  head = Coord(0, 0)
  tail = Coord(0, 0)
  visited = set()
  visited.add(tail)

  file = open('input.txt')

  for line in file:
    tokens = line.strip().split(' ')
    direction = tokens[0]
    numMoves = int(tokens[1])

    for _ in range(0, numMoves):
      prevHead = head.clone()
      head.bump(direction)
      distance = head.distance(tail)

      if distance > 2 or (distance == 2 and head.onSameAxis(tail)):
        tail = prevHead
        visited.add(tail)

  file.close()
  print(len(visited))


if __name__ == "__main__":
  main()