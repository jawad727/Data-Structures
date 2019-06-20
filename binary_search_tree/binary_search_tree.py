class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    # Don't forget to wrap the value in a node.

    if value < self.value: # if the value we pass in is less than the value of the current node execute the following
      
      if not self.left: # if the left child on the node doesn't exist than we will create a new node and set it to become the left child
        self.left = BinarySearchTree(value) 
        
      else: # if the left child does exist then we use recursion and check if it is less or greater than that node and then try to place it in whichever
        self.left.insert(value)

    elif value > self.value: # if the value we pass in is greater than the value of the current node execute the following

      if not self.right: # if the value to the right of the node doesn't exist we create a new node and put it in that place
        self.right = BinarySearchTree(value)
      
      else: # if the value to the right of the node does exist we use recursion and try again on the next node
        self.right.insert(value)
    
    else:
      print("This value already exists, try again")

  def contains(self, target):
  # base case: target == self.value return True
    if target == self.value:
      return True
    
  # If we've traversed down to a node where there is no right or left node, return False
    if not self.right and not self.left:
        return False
      
    if target > self.value: # if the target is greater than the value of the current node execute the following 

      if not self.right: # if the target is greater than the value of the current node AND there is no right child (somthing greater), return false
        return False
     
      else: # if the target is greater than the value of the current node AND there is a right child we will run recursion until it returns somthing
        return self.right.contains(target)
        
    elif target < self.value: # if the target is less than the value of the current node execute the following (same thing as above but with left all the way down)
      if not self.left: 
        return False
      else:
        return self.left.contains(target)

  def get_max(self):
   
    if not self.value: # if there is no current value return this message
      return 'BinarySearchTree needs at least one value before you can preform this operation'

    else: 
      current_max = self.value # starting from the root and setting the current value to the max, if any other is greater it will later replace this one
   
    if not self.right: # if there is nothing to the right of this node (nothing to compare it to) we will return the current max
      return current_max
    
    if self.right.value > current_max: # if the value to the right is greater than the value of the current node we will recurse through the right value
      return self.right.get_max()

    else: # in any other case return the current max
      return current_max

  def for_each(self, cb):
    # inside for_for each we build a helper function called traverse, that takes in a node.
    # We then call traverse, and pass in the current node (which should be the root node)
    def traverse(node): 
      # If the current node is None return out of traverse.
      if not node:
        return
      # call the cb function passing in the current node.value
      cb(node.value)
      # Recursively call traverse on the left node
      traverse(node.left)
      # Recursively call traverse on the right node.
      traverse(node.right)
    # for_each retruns traverse, passing in the root node.
    return traverse(self)