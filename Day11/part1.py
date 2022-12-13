NUM_ROUNDS = 20

class Monkey:
  def __init__(self, items, operator, constant, divisor, trueIndex, falseIndex):
    self.items = items
    self.operator = operator
    self.constant = constant
    self.divisor = divisor
    self.trueIndex = trueIndex
    self.falseIndex = falseIndex
    self.inspections = 0
  
  def inspect(self):
    self.inspections += 1
    item = self.items.pop(0)
    worryLevel = self.performOperation(item) // 3

    if worryLevel % self.divisor == 0:
      return [self.trueIndex, worryLevel]
    else:
      return [self.falseIndex, worryLevel]
  
  def performOperation(self, item):
    operation = None
    constant = None

    if self.operator == '+':
      operation = add
    elif self.operator == '*':
      operation = multiply
    
    if self.constant == 'old':
      constant = item
    else:
      constant = int(self.constant)
    
    return operation(constant, item)
  
  def __lt__(self, other):
    return self.inspections < other.inspections

def add(x, y):
  return x + y

def multiply(x, y):
  return x * y

def main():
  with open('input.txt') as file:
    first = file.readline()
    monkeys = []

    while first != '':
      itemsLine = file.readline().strip().split(': ')
      items = [int(item) for item in itemsLine[1].split(', ')]

      operation = file.readline().strip().split(' ')
      operator = operation[-2]
      constant = operation[-1]

      test = file.readline().strip().split(' ')
      divisor = int(test[-1])

      trueIndex = int(file.readline().strip().split(' ')[-1])
      falseIndex = int(file.readline().strip().split(' ')[-1])

      monkeys.append(Monkey(items, operator, constant, divisor, trueIndex, falseIndex))

      file.readline()
      first = file.readline()

  for x in range(0, NUM_ROUNDS):
    for monkey in monkeys:
      while len(monkey.items) > 0:
        [index, item] = monkey.inspect()
        monkeys[index].items.append(item)
    
  monkeys.sort(reverse=True)
  monkeyBusiness = monkeys[0].inspections * monkeys[1].inspections
  print(monkeyBusiness)

if __name__ == '__main__':
  main()