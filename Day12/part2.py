ASCII_OFFSET = 97

class Node:
  def __init__(self, elevation, end, x, y, char):
    self.elevation = elevation
    self.end = end
    self.x = x
    self.y = y
    self.char = char
    self.minDistance = None
  
  def __hash__(self):
    return hash(str(self.x) + ',' + str(self.y))
  
  def __eq__(self, other):
    return self.x == other.x and self.y == other.y
  
  def __lt__(self, other):
    return self.minDistance < other.minDistance

  def __repr__(self):
    return 'Node (minDistance: ' + str(self.minDistance) + ', x: ' + str(self.x) + ', y: ' + str(self. y) + ', char: ' + self.char + ')'

def getNeighbors(grid, x, y):
  maxY = len(grid)
  maxX = len(grid[0])
  coords = [[0, 1], [0, -1], [1, 0], [-1, 0]]
  neighbors = []

  for coord in coords:
    newX = x + coord[0]
    newY = y + coord[1]

    if newX >= 0 and newX < maxX and newY >= 0 and newY < maxY:
      neighbors.append(grid[newY][newX])
  
  return neighbors

def main():
  grid = []
  y = 0
  startNodes = [] 
  endNode = None
  file = open('/Users/dkavalchek/codingProjects/AdventOfCode2022/Day12/input.txt')

  for line in file:
    row = []
    line = line.strip()
    for x in range(0, len(line)):
      char = line[x]

      if char == 'E':
        endNode = Node(ord('z') - ASCII_OFFSET, True, x, y, char)
        row.append(endNode)
      elif char == 'a':
        node = Node(0, False, x, y, char)
        startNodes.append(node)
        row.append(node)
      else:
        row.append(Node(ord(char) - ASCII_OFFSET, False, x, y, char))

    y += 1
    grid.append(row)

  file.close()

  minSteps = None

  for startNode in startNodes:
    for row in grid:
      for node in row:
        node.minDistance = None
    startNode.minDistance = 0

    visited = set([startNode])
    queue = [startNode]

    while len(queue) > 0:
      queue.sort()
      node = queue.pop(0)
      neighbors = getNeighbors(grid, node.x, node.y)

      for neighbor in neighbors:
        elevationDiff = neighbor.elevation - node.elevation
        currentDistance = node.minDistance + 1

        if elevationDiff <= 1:
          if neighbor.minDistance == None or neighbor.minDistance > currentDistance:
            neighbor.minDistance = currentDistance
            queue.append(neighbor)

          if neighbor not in visited:
            visited.add(neighbor)
    
    if minSteps == None or (endNode.minDistance != None and endNode.minDistance < minSteps):
      minSteps = endNode.minDistance
    
  
  print(minSteps)


if __name__ == '__main__':
  main()