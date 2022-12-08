
class Tree:
  def __init__(self, height, x, y, grid):
    self.height = height
    self.x = x
    self.y = y
    self.grid = grid
    self.visible = None
  
  def findIsVisible(self):
    gridHeight = len(self.grid);
    gridWidth = len(self.grid[0])

    if self.x == gridWidth-1 or self.x == 0 or self.y == gridHeight-1 or self.y == 0:
      print('I am an edge tree')
      self.visible = True
      return True
    else:
      coords = [[0, 1], [0, -1], [1, 0], [-1, 0]]

      for coord in coords:
        x = coord[0]
        y = coord[1]

        tree = self.grid[y][x]
        treeVisible = tree.visible 

        if treeVisible == None:
          treeVisible = tree.findIsVisible()
        
        if treeVisible and self.height > tree.height:
          print(self.x + x, self.y + y, ' I am bigger and they are visible')
          self.visible = True
          return True
      
      self.visible = False
      return False

def main():
  file = open('/Users/dkavalchek/codingProjects/AdventOfCode2022/Day08/testInput.txt')

  grid = []
  y = 0

  for line in file:
    row = []
    line = line.strip()
    for x in range(0, len(line)):
      height = int(line[x])
      row.append(Tree(height, x, y, grid))

    grid.append(row)
    y += 1

  file.close()
  gridHeight = len(grid);
  gridWidth = len(grid[0])
  count = 0

  for y in range(0, gridHeight):
    for x in range(0, gridWidth):
      tree = grid[y][x]
      treeVisible = tree.visible
      
      if treeVisible == None:
        treeVisible = tree.findIsVisible()
      
      if treeVisible:
        count += 1
  
  print(count)

if __name__ == '__main__':
  main()