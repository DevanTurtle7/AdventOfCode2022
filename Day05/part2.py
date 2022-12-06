COL_WIDTH = 4

def main():
  with open('/Users/dkavalchek/codingProjects/AdventOfCode2022/Day05/input.txt') as file:
    line = file.readline()
    first = True
    stacks = []
    numCols = len(line) // COL_WIDTH

    while line[1] != '1':
      if first:
        first = False
        for _ in range(0, numCols): stacks.append([])

      for i in range(0, len(line), COL_WIDTH):
        item = line[i : i + COL_WIDTH].strip()

        if item != '':
          item = item[1]
          stacks[i // COL_WIDTH].append(item)

      line = file.readline()

    for i in range(0, numCols): stacks[i].reverse()
  
    line = file.readlines(3)[1]

    while line != '':
      tokens = line.strip().split(' ')
      count = int(tokens[1])
      fromCol = int(tokens[3]) - 1
      toCol = int(tokens[5]) - 1

      stacks[toCol].extend(stacks[fromCol][-count::])
      stacks[fromCol] = stacks[fromCol][:-count:]

      line = file.readline()

    string = ''

    for stack in stacks:
      if len(stack) > 0:
        string += stack.pop()

    print(string)

if __name__ == '__main__':
  main()
