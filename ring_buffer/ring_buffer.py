class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

    #how do we know the oldest value?
    #answer:self.current
    #deletion and insertion are most performant with linked lists
    #but it appears storage is already an array. So we can go with that
  def append(self, item):
    '''if our list is at capacity, pop oldest element,
    which is tracked by the current. Current should be
    reset or incremented depending on its value'''
   

    
    if self.current > (self.capacity -1):
      self.current = 0
      self.storage[self.current] = item
      self.current +=1
    else:
      self.storage[self.current] = item
      self.current +=1

    #any other cases?

    

  def get(self):
    return [item for item in self.storage if item != None]
    
    '''returns list values in curernt order
    without None values'''
    