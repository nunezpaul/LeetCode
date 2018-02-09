'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Credits:
Special thanks to @ts for adding this problem and creating all test cases.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        threshold = len(nums)
        
        count = {}
        
        for i in nums:
            if i in count:
                count[i]+=1
                if count[i] > threshold/2:
                    return i
            
            else:
                count[i]=1
        
        return max(count)
        
