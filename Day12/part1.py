ASCII_OFFSET = 97

class Node:
  def __init__(self, elevation, end, x, y):
    self.elevation = elevation
    self.end = end
    self.x = x
    self.y = y
    self.minDistance = None
  
  def __hash__(self):
    return self.x ** (self.y ** 2)
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y

  def __repr__(self):
    return str(self.minDistance)

class NodePriorityQueue:
  def __init__(self):
    self.items = []
  
  def insert(self, item):
    # Insert reversed
    upperBound = len(self.items)
    lowerBound = 0

    while upperBound - lowerBound > 1 and upperBound > lowerBound:
      diff = upperBound - lowerBound
      midIndex = lowerBound + (diff // 2)
      midPoint = self.items[midIndex].minDistance

      if midPoint == item.minDistance:
        self.items.insert(midIndex, item)
        break;
      elif midPoint > item.minDistance:
        lowerBound = midPoint
      else:
        upperBound = midPoint
    
    print(upperBound, lowerBound, self.items, item.minDistance)
    self.items.insert(upperBound, item)
  
  def pop(self):
    return self.items.pop()

def main():
  grid = []
  startX = None
  startY = None

  file = open('input.txt')
  y = 0
  startNode = None

  for line in file:
    row = []
    line = line.strip()
    for x in range(0, len(line)):
      char = line[x]

      if char == 'E':
        row.append(Node(0, True, x, y))
      elif char == 'S':
        node = Node(0, False, x, y)
        startNode = node
        row.append(node)
      else:
        row.append(Node(ord(char) - ASCII_OFFSET, False, x, y))

    y += 1
    grid.append(row)

  file.close()
  endReached = False
  queue = NodePriorityQueue()
  visited = set([startNode])
  queue.insert(startNode)
  maxWidth = len(grid[0])
  maxHeight = len(grid)

  while not endReached:
    current = queue.pop()
    neighborCoords = [[0, 1], [1, 0], [0, -1], [-1, 0]]

    for coords in neighborCoords:
      x = current.x + coords[0]
      y = current.y + coords[1]
      print(x, y)
      if x > 0 and y > 0 and x < maxWidth and y < maxHeight:
        node = grid[y][x]

        if node not in visited:
          elevationDiff = abs(node.elevation - current.elevation)
          if elevationDiff <= 1 and (node.minDistance == None or node.minDistance < elevationDiff):
            node.minDistance = elevationDiff
            queue.insert(node)
            visited.add(node)


if __name__ == '__main__':
  main()