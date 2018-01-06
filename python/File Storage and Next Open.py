'''

Develop a system that keeps track of Disk that is subdivided in N partitions. 
Function writeData(position), will fill that position and should be marked as unavailable. Return 1 if available or -1 if not.
Function nextOpen(position), will find the next open position available for data to be written to. If the position has data written to it then return -1 otherwise return the position of the next available slot.

Example:

writeData(10) -> 1
writeData(10) -> -1
nextOpen(10) -> -1
nextOpen(9) -> 11

'''

class Node(object):
  def __init__(self, x):
    self.val = x
    self.next = None
    self.prev = None
    
class fileSystem(object):
  def __init__(self, x):
    if x < 1:
      return "ERROR"
    self.partions = x
    self.open = {0:Node(0)}
    for i in range(1,x):
      self.open[i] = Node(i)
      self.open[i].prev = self.open[i-1]
      self.open[i-1].next = self.open[i]
    self.filled = {}
    
  def writeData(position):
    if position not in self.open:
      return -1
    #remove pointers going to that position and reroute them around it
    self.open[position].prev.next = self.open[position].next
    self.open[position].next.prev = self.open[position].prev
    filled[position] = open[position]
    del(open[position])
    return 1
    
  def nextOpen(position):
    if position not in self.open:
      return -1
    return open[position].next.val
      
      
