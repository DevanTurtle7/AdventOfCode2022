
def main():
  file = open('./input.txt')

  for line in file:
    for i in range(4, len(line)):
      chars = set()
      match = False

      for char in line[i-4:i]:
        if char in chars:
          match = True
          break;

        chars.add(char)
      
      if not match:
        print(i)
        break



  file.close()

if __name__ == "__main__":
  main()