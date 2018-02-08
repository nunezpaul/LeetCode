'''
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in linear time and in O(1) space.
'''

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        threshold = len(nums)/3
        store = {}
        
        for i in nums:
            if i in store:
                store[i]+=1
            else:
                store[i] =1
        
        greaterThanThreshold = []
        
        for i in store:
            if store[i]>threshold:
                greaterThanThreshold.append(i)
        
        return greaterThanThreshold
