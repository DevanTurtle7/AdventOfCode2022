def parseInnerList(line, index):
  list = []
  endFound = False
  i = index + 1
  current = ""

  while i < len(line) and not endFound:
    char = line[i]

    if char == '[':
      [innerList, endIndex] = parseInnerList(line, i)
      list.append(innerList)
      i = endIndex
    elif char == ']':
      endFound = True;
    elif char == ',':
      if current != '':
        list.append(int(current))
        current = ''
    else:
      current += char
    
    if not endFound:
      i += 1
    
  if current != '':
    list.append(int(current))

  return [list, i]


def parseLine(line):
  line = line.strip()

  return parseInnerList(line, 0)[0]

def compareLists(leftList, rightList):
  ordered = None
  i = 0

  while i < len(leftList) and i < len(rightList) and ordered == None:
    left = leftList[i]
    right = rightList[i]

    if isinstance(left, int) and isinstance(right, int):
      if left > right:
        ordered = False
      if left < right:
        ordered = True
    elif isinstance(left, list) and isinstance(right, list):
      ordered = compareLists(left, right)
    elif isinstance(left, list) and isinstance(right, int):
      ordered = compareLists(left, [right])
    elif isinstance(left, int) and isinstance(right, list):
      ordered = compareLists([left], right)
    else:
      print('Err: Unknown combo')

    i += 1

  if ordered == None:
    if len(leftList) == len(rightList):
      return None
    elif i >= len(leftList):
      return True
    else:
      return False
  else:
    return ordered

def main():
  total = 0

  with open('input.txt') as file:
    eof = False
    count = 1

    while not eof:
      leftPacket = parseLine(file.readline())
      rightPacket = parseLine(file.readline())

      if compareLists(leftPacket, rightPacket):
        total += count

      if file.readline() == '':
        eof = True
      else:
        count += 1
  
  print(total)

if __name__ == '__main__':
  main()