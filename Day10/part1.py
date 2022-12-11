class CPU:
  def __init__(self):
    self.cycle = 1
    self.x = 1
    self.total = 0
    self.importantCycles = set([20, 60, 100, 140, 180, 220])
  
  def incrementCycle(self):
    self.checkX()
    self.cycle += 1
  
  def addX(self, count):
    self.x += count
  
  def checkX(self):
    if self.cycle in self.importantCycles:
      signalStrength = (self.x * self.cycle)
      self.total += signalStrength

def main():
  file = open('./input.txt')
  cpu = CPU()

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
  print(cpu.total)

if __name__ == '__main__':
  main()