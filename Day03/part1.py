
def main():
  file = open('input.txt')
  total = 0

  for line in file:
    line = line.strip()
    half = len(line) // 2
    first = line[0:half]
    second = line[half::]
    compartment = set()

    for char in first:
      compartment.add(char)

    for char in second:
      if char in compartment:
        value = ord(char)

        if value > 90:
          total += value - 96
        else:
          total += value - 38
        break
    
  file.close()
  print(total)

if __name__ == '__main__':
  main()