DRAW_POINTS = 3
WIN_POINTS = 6

class Item:
  def __init__(self, points):
    self.beats = None
    self.losses = None
    self.points = points


def beats(winner, losser):
  winner.beats = losser
  losser.losses = winner

def main():
  file = open('input.txt')
  points = 0

  rock = Item(1)
  paper = Item(2)
  scissors = Item(3)
  beats(rock, scissors)
  beats(scissors, paper)
  beats(paper, rock)

  translator = {
    'A': rock,
    'B': paper,
    'C': scissors
  }

  for line in file:
    tokens = line.strip().split(' ')
    opp = translator[tokens[0]]
    result = tokens[1]

    if result == 'X':
      points += opp.beats.points
    elif result == 'Y':
      points += opp.points + DRAW_POINTS
    elif result == 'Z':
      points += opp.losses.points + WIN_POINTS

  file.close()
  print(points)

if __name__ == '__main__':
  main()