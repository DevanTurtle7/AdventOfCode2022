TOTAL_DISK_SPACE = 70000000
REQUIRED_UNUSED_SPACE = 30000000

class Directory:
  def __init__(self, name):
    self.name = name
    self.children = []
    self.parent = None
    self.count = 0
  
  def addChild(self, child):
    self.children.append(child)
    child.parent = self
  
  def cd(self, directoryName):
    for directory in self.children:
      if directory.name == directoryName:
        return directory
  
  def updateCount(self):
    count = 0

    for child in self.children:
      if type(child) is File:
        count += child.size
      else: 
        child.updateCount()
        count += child.count
    
    self.count = count

class File:
  def __init__(self, name, size):
    self.name = name
    self.size = size

def bfs(root):
  queue = []
  visited = set()
  queue.append(root)
  closestDir = root
  closest = TOTAL_DISK_SPACE

  spaceRemaining = TOTAL_DISK_SPACE - root.count
  spaceNeeded = REQUIRED_UNUSED_SPACE - spaceRemaining

  while len(queue) > 0:
    directory = queue.pop()
    visited.add(directory)
    extraSpace = directory.count - spaceNeeded 

    if extraSpace < closest and extraSpace > 0:
      closest = extraSpace
      closestDir = directory

    for child in directory.children:
      if type(child) is Directory and child not in visited:
        queue.append(child)
  
  print(closestDir.count)

def main():
  with open('input.txt') as file:
    line = file.readline()
    workingDirectory = Directory('/')

    while line != '':
      tokens = line.strip().split(' ')
      command = tokens[1]

      if command == "cd":
        directory = tokens[2]

        if directory == '..':
          workingDirectory = workingDirectory.parent
        elif directory == '/':
          pass
        else:
          workingDirectory = workingDirectory.cd(directory)

        line = file.readline()
      elif command == 'ls':
        printLine = file.readline()

        while printLine != '' and printLine[0] != '$':
          tokens = printLine.strip().split(' ')

          if tokens[0] == 'dir':
            workingDirectory.addChild(Directory(tokens[1]))
          else:
            workingDirectory.addChild(File(tokens[1], int(tokens[0]))) 

          printLine = file.readline()
          line = printLine

    while workingDirectory.parent != None:
      workingDirectory = workingDirectory.parent
    
    workingDirectory.updateCount()
    bfs(workingDirectory)

if __name__ == '__main__':
  main()