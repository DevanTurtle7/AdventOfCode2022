
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


def searchFiles (directory):
  count = 0

  if directory.count <= 100000:
    count += directory.count

  for child in directory.children:
    if type(child) is Directory:
      count += searchFiles(child)

  return count

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
    print(searchFiles(workingDirectory))

if __name__ == '__main__':
  main()