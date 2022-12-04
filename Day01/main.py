
def main():
  file = open('./input.txt')
  cal = 0
  maxCal = 0

  for line in file:
    if line == '\n':
      if cal > maxCal:
        maxCal = cal

      cal = 0
    else:
      cal += int(line)

  file.close()
  print(maxCal)

if __name__ == '__main__':
  main()