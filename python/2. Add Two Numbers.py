'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class Solution(object):
    def __init__(self):
        self.carry = False
    
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        if l1 == None and l2 == None:
            if self.carry:
                return ListNode(1)
            return None
        
        if l1 != None and l2 == None:
            add = ListNode(l1.val)
            
            if self.carry:
                add.val += 1
                self.carry = False
                
            if add.val > 9:
                add.val -= 10
                self.carry = True
                
            add.next = self.addTwoNumbers(l1.next, None)
            return add
                            
        if l2 != None and l1 == None:
            add = ListNode(l2.val)
            
            if self.carry:
                add.val += 1
                self.carry = False
                
            if add.val > 9:
                add.val -= 10
                self.carry = True
                
            add.next = self.addTwoNumbers(None, l2.next)
            return add
        
        else:
            add = ListNode(l1.val + l2.val)
            if self.carry:
                add.val+=1
                self.carry = False
            if add.val > 9:
                add.val-=10
                self.carry = True
            add.next = self.addTwoNumbers(l1.next, l2.next)
            return add


#O(n + m) time
