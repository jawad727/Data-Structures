class Node:

  def __init__(self, value=None, next_node=None):
    self.value = value
    self.next_node = next_node

  def get_value(self):
    return self.value
  
  def get_next(self):
    return self.next_node

  def set_next(self, new_next):
    self.next_node = new_next

  def __str__(self):
    return f'Value: {self.value}, Next Node: {self.next_node}'
  




class LinkedList: # creating a list class

  def __init__(self): # the list will have a head and a tail
    self.head = None
    self.tail = None


  def add_to_tail(self, value): # creating a method to add to the tail
    new_node = Node(value, None) # the new node that we add will have a value of the new value

    if not self.head: # if head doesnt exist then the new linked list will start at the new value
      self.head = new_node
      self.tail = new_node
    else: # if a head does exist then the previous tail will set its "next_tail:" to the new_node and and the new tail will be set to the new_node
      self.tail.set_next(new_node)
      self.tail = new_node


  def remove_head(self): # creating a method to remove the head
    if not self.head:
      return None # if the head doesnt exist neither does anything else so return None

    if not self.head.get_next(): # if the next value after the head node doesnt exist make the head equal to nothing and return that value (because you essentially popped off the last value)
      head = self.head 
      self.head = None
      self.tail = None
      return head.get_value()

    value = self.head.get_value() # value is set to the head at the moment we call it
    self.head = self.head.get_next() # here we set the head to the values of the next node that comes after head
    return value # here we return value (the new head)


  def contains(self, value): # this method checks to see if we have a certain value in the linked list
    if not self.head:
      return False
    
    current = self.head

    while current: # iteration through the linked list
      if current.get_value() == value:
        return True

      current = current.get_next() #this here is how it iterates through

    return False


  def length_of(self):
    incr = 0
    current = self.head
    while current:
      incr += 1
      current = current.get_next()
    return incr


  def __str__(self):
    return f'{self.head}, {self.tail}'





class Queue:
  def __init__(self):
    # what data structure should we
    # use to store queue elements?
    self.storage = LinkedList()

  def enqueue(self, item):
    return self.storage.add_to_tail(item)
  
  def dequeue(self):
    return self.storage.remove_head()

  def len(self):
    return self.storage.length_of()

  def __str__(self):
    return f'{self.storage}'


foo = Queue()

print(foo.len())


