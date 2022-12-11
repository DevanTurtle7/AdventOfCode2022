def day(day: int) -> str:
	with open(f"input.txt") as file:
		return file.read()

input = [(line.split()[0], int(line.split()[1])) for line in day(9).splitlines()]


def get_vector_change(direction: str):
  if direction == 'L':
    return [-1, 0]
  elif direction == 'U':
      return [0, 1]
  elif 'R':
      return [1, 0]
  elif 'D':
      return [0, -1]
  else :
      print("Invalid direction argument")
      exit(-1)


def move_tail(head, tail):
    Δ = [x - y for x, y in zip(head, tail)]

    if abs(Δ[0]) > 1 or abs(Δ[1]) > 1:
        tail[:] = [n + (1 if Δn >= 1 else -1 if Δn <= -1 else 0) for n, Δn in zip(tail, Δ)]


head = [0, 0]
tail = [0, 0]

tail_parts = [[0, 0] for _ in range(9)]

visited_p1 = set()
visited_p2 = set()

for direction, amount in input:
    for i in range(amount):
        head = [x + y for x, y in zip(head, get_vector_change(direction))]

        move_tail(head, tail)
        visited_p1.add(tuple(tail))

        for i in range(len(tail_parts)):
            move_tail(head if i == 0 else tail_parts[i - 1], tail_parts[i])

            if i == 8:
                visited_p2.add(tuple(tail_parts[i]))

print(f"Part 1: {len(visited_p1)}")
print(f"Part 2: {len(visited_p2)}")