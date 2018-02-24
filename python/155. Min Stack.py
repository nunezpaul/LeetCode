'''

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.

'''

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.hold = []
        self.hold_min = float('inf')

    def push(self, x):
        """
        O(1)
        :type x: int
        :rtype: void
        """
        self.hold.append(x)
        
        if x < self.hold_min:
            self.hold_min = x
            
    def pop(self):
        """
        worst: O(N)
        best: O(1)
        :rtype: void
        """
        self.hold.pop()
        if len(self.hold) > 0:
            self.hold_min = min(self.hold)
        
        else:
            self.hold_min = float('inf')
        
    
    def top(self):
        """
        O(1)
        :rtype: int
        """

        return self.hold[-1]

    def getMin(self):
        """
        O(1)
        :rtype: int
        """
        
        return self.hold_min
