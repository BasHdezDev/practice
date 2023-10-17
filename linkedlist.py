class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
    self.size = 0

  def add_head(self, value):
    new_node = Node(value)
    if self.size == 0:
      self.head = new_node
      self.size += 1
    else:
      new_node.next = self.head
      self.head = new_node
      self.size += 1
