'''

Given a singly linked list, determine if it is a palindrome.

O(n) time 
O(n) space

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    
    
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        track = []
        length = 1
        
        if (head is None):
            return True
        
        track.append(head.val)
        
        while head.next is not None:
            head = head.next
            track.append(head.val)
            length +=1
            
        half = length / 2
        if length % 2 == 0: #if even then both halves should be the same
            left = track[:half]
            right = track[half:]
        else: #if odd then they should be the same around the center
            left = track[:half]
            right = track[half+1:]
          
        #print(half)
        for i,j in enumerate(reversed(left)):
            #print(j, right[i])
            if j!=right[i]:
                return False
        
        return True
            
        
