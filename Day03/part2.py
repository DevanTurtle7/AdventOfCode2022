def priority(char):
  value = ord(char)

  if value > 90:
    return value - 96
  else:
    return value - 38


def main():
  file = open('/Users/dkavalchek/codingProjects/AdventOfCode2022/Day03/input.txt')
  total = 0
  index = 0

  shared = set()

  for line in file:
    current = set()

    for char in line.strip():
      if index % 3 == 0:
        current.add(char)      
      else:
        if char in shared:
          current.add(char)

    shared = current

    if index % 3 == 2:
      for char in shared:
        total += priority(char)

    index += 1
    
  file.close()
  print(total)

if __name__ == '__main__':
  main()