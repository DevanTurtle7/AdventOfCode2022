class Node:
  def __init__(self, value):
    self.next = None;
    self.prev = None;
    self.value = value;
  
  def insert(self, node):
      if node.value < self.value:
        if self.next is None:
          self.next = node
          node.prev = self
        else:
          self.next.insert(node)
      else:
        if self.prev is not None:
          self.prev.next = node

        node.prev = self.prev
        node.next = self
        self.prev = node
    

class LinkedList:
  def __init__(self):
    self.head = None

  def insert(self, node):
    if self.head is None:
      self.head = node
    else:
      self.head.insert(node)

      if self.head.prev is not None:
        self.head = self.head.prev
  
  def popMax(self):
    node = self.head
    index = 0

    while node is not None:
      if index == 2:
        node.next = None 
        break

      node = node.next
      index += 1
  
  def total(self):
    node = self.head
    count = 0

    while node is not None:
      count += node.value
      node = node.next
    
    return count

  def __repr__(self):
    string = '['
    node = self.head

    while node is not None:
      string += str(node.value) + ', '
      node = node.next

    string += ']'

    return string

def main():
  file = open('/Users/dkavalchek/codingProjects/AdventOfCode2022/Day01/input.txt')
  cal = 0
  list = LinkedList()

  for line in file:
    if line == '\n':
      list.insert(Node(cal))
      list.popMax()

      cal = 0
    else:
      cal += int(line)

  file.close()
  print(list)
  print(list.total())

if __name__ == '__main__':
  main()