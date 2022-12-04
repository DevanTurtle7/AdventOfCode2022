
def main():
  file = open('input.txt')
  count = 0

  for line in file:
    tokens = line.strip().split(',')
    pair1Tokens = tokens[0].split('-')
    pair2Tokens = tokens[1].split('-')
    min1 = int(pair1Tokens[0])
    max1 = int(pair1Tokens[1])
    min2 = int(pair2Tokens[0])
    max2 = int(pair2Tokens[1])
    minDiff = min1 - min2 
    maxDiff = max1 - max2

    if (minDiff <= 0 and maxDiff >= 0) or (minDiff >= 0 and maxDiff <= 0):
      count += 1
   
  file.close()
  print(count)

if __name__ == '__main__':
  main()