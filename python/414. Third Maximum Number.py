"""

Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.

O(n) solution
"""

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #First is highest and third is lowest
        
        first = None
        second = None
        third = None
        
        for i in nums:
            if not(i in [first, second, third]):
                if i > first:
                    second, third = first, second
                    first = i

                elif i > second:
                    third = second
                    second = i

                elif i > third:
                    third = i
                
        print(first, second, third)
        if third is not None:    
            return third
            
        else:
            return first
