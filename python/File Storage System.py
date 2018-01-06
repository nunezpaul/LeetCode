'''

Develop a system that keeps track of Disk that is subdivided in N partitions. 
Function writeData(position), will fill that position and should be marked as unavailable. Return 1 if available or -1 if not.
Function nextOpen(position), will find the next open position available for data to be written to. If the position has data written to it then return -1 otherwise return the position of the next available slot.
Function deleteData(position), will mark that a position open and available for data to be written to. Return 1 if data was deleted or -1 if alraedy empty.

Example:
test = fileSystem(10)

test.nextOpen(9) -> 10
test.writeData(10) -> 1
test.writeData(10) -> -1
test.nextOpen(10) -> -1
test.nextOpen(9) -> 11
test.deleteData(9) -> -1
test.deleteData(10) -> 1
test.nextOpen(9) -> 10

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
    #Depiction of writeData(n)
    #                   Before:
    #      _______       _______       _______
    #     |       | ->  |       | ->  |       |
    #     |  n-1  |     |   n   |     |  n+1  |
    #     |_______| <-  |_______| <-  |_______|
    #
    #                     After:
    #          ___________________________
    #         |    filled[n].prev.next    | 
    #      ___|___       _______       ___v___
    #     |       |     |       | ->  |       |
    #     |  n-1  |     |   n   |     |  n+1  |
    #     |_______| <-  |_______|     |_______|
    #         ^                           |
    #         |    filled[n].next.prev    |
    #         |___________________________|
  
  
  def deleteData(position):
    if position not in self.filled:
      return -1
    self.filled.prev
    #reattach pointers such that the position of the filled data around it points towards it 
    self.filled[position].prev.next = self.filled[position]
    self.filled[position].next.prev = self.filled[position]
    open[position] = filled[position]
    del(filled[position])
    return 1

    #Depiction of deleteData(n)
    #                   Before:
    #          ___________________________
    #         |    filled[n].prev.next    | 
    #      ___|___       _______       ___v___
    #     |       |     |       | ->  |       |
    #     |  n-1  |     |   n   |     |  n+1  |
    #     |_______| <-  |_______|     |_______|
    #         ^                           |
    #         |    filled[n].next.prev    |
    #         |___________________________|
    #
    #                     After:
    #      _______       _______       _______
    #     |       | ->  |       | ->  |       |
    #     |  n-1  |     |   n   |     |  n+1  |
    #     |_______| <-  |_______| <-  |_______|    
    
  def nextOpen(position):
    if position not in self.open:
      return -1
    return open[position].next.val
      
      
