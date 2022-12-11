WIDTH = 40

class CPU:
  def __init__(self, crt):
    self.cycle = 1
    self.x = 1
    self.total = 0
    self.crt = crt
  
  def incrementCycle(self):
    self.crt.drawDisplay(self.cycle, self.x)
    self.cycle += 1
  
  def addX(self, count):
    self.x += count

class CRT:
  def __init__(self):
    self.display = ''
  
  def drawDisplay(self, cycle, x):
    pixel = (cycle - 1)
    widthAdded = pixel - (pixel % WIDTH)
    pixel -= widthAdded
    diff = abs(pixel - x)

    if diff <= 1:
      self.display += '#'
    else:
      self.display += '.'

    if cycle % WIDTH == 0:
      self.display += '\n'

def main():
  file = open('./input.txt')
  crt = CRT()
  cpu = CPU(crt)

  for line in file:
    tokens = line.strip().split(' ')
    command = tokens[0]

    if command == 'noop':
      cpu.incrementCycle()
    elif command == 'addx':
      cpu.incrementCycle()
      cpu.incrementCycle()
      count = int(tokens[1])
      cpu.addX(count)

  file.close()
  print(crt.display)

if __name__ == '__main__':
  main()