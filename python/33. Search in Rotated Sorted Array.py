'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.
'''

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        num_hash = set(nums)
        split = len(nums)/2
        
        if target in num_hash and len(nums) > 1:
            left = nums[:split]
            right = nums[split:]
            
            l_index = 0
            r_index = 0
            
            if target in left:
                l_index = self.search(left, target)
                split = 0
            else:
                r_index = self.search(right, target)
            
            return split + l_index + r_index
        
        elif target in num_hash:
            return 0
        
        else:
            return -1
            
#O(logN) time
