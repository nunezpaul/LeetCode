'''

Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

O(n) time
O(1) space

'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        #sum the numbers and subtract the total from what it should be
        
        nums_sum = 0
        expected_sum = 0
        for index, i in enumerate(nums):
            nums_sum += i
            expected_sum += index
            
        expected_sum += index+1
        
        missing = expected_sum - nums_sum
        
        return missing
