DRAW_POINTS = 3
WIN_POINTS = 6

TRANSLATOR = {
  'A': 'rock',
  'X': 'rock',
  'B': 'paper',
  'Y': 'paper',
  'C': 'scissors',
  'Z': 'scissors',
}

POINTS = {
  'rock': 1,
  'paper': 2,
  'scissors': 3
}

BEATS = {
  'rock': 'scissors',
  'scissors': 'paper',
  'paper': 'rock',
}

def main():
  file = open('input.txt')
  points = 0

  for line in file:
    tokens = line.strip().split(' ')
    opp = TRANSLATOR[tokens[0]]
    me = TRANSLATOR[tokens[1]]

    points += POINTS[me]

    if opp == me:
      points += DRAW_POINTS
    elif BEATS[me] == opp:
      points += WIN_POINTS

  file.close()
  print(points)

if __name__ == '__main__':
  main()