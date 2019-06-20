"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:

  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value): #pass in a value ('bar')
    current_next = self.next #this variable equals the next value (None)
    self.next = ListNode(value, self, current_next) #next is set to a listnode with 'bar' as the value
    if current_next: #if current next exists set current_next.prev to the next value
      current_next.prev = self.next
      
  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev


  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev


  def __repr__(self):
    return f'{self.value}'




"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""

class DoublyLinkedList:

  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.length = 1 if node is not None else 0

  def __len__(self):
    return self.length

  def add_to_head(self, value):
    self.length += 1
    prev_head = self.head
    self.head = ListNode(value, None , prev_head)
    prev_head.prev = self.head

  def remove_from_head(self):
    self.length -= 1
    self.head = self.head.next
    self.head.prev = None

  def add_to_tail(self, value):
    self.length += 1
    prev_tail = self.tail
    self.tail = ListNode(value, prev_tail , None)
    prev_tail.prev = self.head

  def remove_from_tail(self):
    self.length -= 1
    self.tail = self.tail.prev
    self.tail.head = None

  def move_to_front(self, node):
    # If the node put in is already the head node.
    if self.head == node:
      return
      # if there's only one node in the list.
    elif node.prev == self.head and node == self.tail:
      old_head = self.head
      self.head = node
      self.head.prev = None
      self.head.next = old_head
      self.tail = old_head
      self.tail.prev = self.head
      self.tail.next = None

    else:
        # Pull current item out of list.
      next_node = node.next
      prev_node = node.prev
      next_node.prev = node.prev
      prev_node.next = node.next
        # Set it to head
      old_head = self.head
      self.head = node
      self.head.next = old_head
      self.head.prev = None
      old_head.prev = self.head

  def move_to_end(self, node):
    pass

  def delete(self, node):
    pass
    
  def get_max(self):
    pass

  def __str__(self):
    return f'\nLength: {self.length} \nHead: {self.head} \nTail: {self.tail}'

foo = DoublyLinkedList(ListNode("1stHead"))

print(foo)

foo.add_to_head("2ndHead")

print(foo)

foo.add_to_tail("0thHead")

print(foo)

foo.delete(ListNode("2ndHead"))

print(foo)

foo.move_to_front(ListNode("0thHead"))