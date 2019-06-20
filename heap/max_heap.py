class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):

    self.storage.append(value)
    self._bubble_up(len(self.storage)-1)

  def delete(self):

    old_prio = self.storage[0]
    self.storage[0], self.storage[-1] = self.storage[-1], self.storage[0]
    del self.storage[-1]
    self._sift_down(0)
    return old_prio

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):

    while index > 0:


        parent = (index -1 ) // 2

        if self.storage[index] > self.storage[parent]:

          self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
 
          index = parent

        else:

          break

  def _sift_down(self, index):

    while index < len(self.storage)-1:
      left_child = (2*index) + 1
      right_child = (2*index) + 2

      try:
        a = self.storage[left_child]
      except IndexError:
        break
      try:
        b = self.storage[right_child]
      except IndexError:
        pass

      try:
        if self.storage[index] < self.storage[left_child] and self.storage[index] < self.storage[right_child]:
          if self.storage[left_child] >= self.storage[right_child]:
            self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
            index = left_child
            continue
          else:
            self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
            index = right_child
            continue
      except IndexError:
        pass


      try:
        if self.storage[index] < self.storage[left_child]:
          self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
          index = left_child
          continue
      except IndexError:
        pass


      try:
        if self.storage[index] < self.storage[right_child]:
          self.storage[index], self.storage[right_child] = self.storage[right_child], self.storage[index]
          index = right_child
          continue
      except IndexError:
        pass


      break