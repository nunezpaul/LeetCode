'''

Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.

Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Therefore, return the max sliding window as [3,3,5,5,6,7].

Note: 
You may assume k is always valid, ie: 1 ≤ k ≤ input array's size for non-empty array.

Follow up:
Could you solve it in linear time?

'''

class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        max_ = -float('inf')
        max_index = None
        
        sliding_window = []
        for i in range(k):
            check = nums.pop(0)
            sliding_window.append(check)
            
            if check > max_:
                max_ = check
                max_index = i
        
        max_window = []
        length = len(nums)#do this only once instead of everytime
        
        if max_ != -float('inf'):
            max_window.append(max_)
        
        while length > 0:
            check = nums.pop(0)
            sliding_window.pop(0)
            sliding_window.append(check)
            max_index-=1
            #print(sliding_window, max_index)


            if max_index > 0:
                
                if check > max_:
                    max_ = check
                    max_index = k-1
                    
            else:
                
                max_ = -float('inf')
                max_index = None
                for i,j in enumerate(sliding_window): #worst cast O(n*k)
                    if j > max_:
                        max_ = j
                        max_index = i
            
            max_window.append(max_)
            
            length-=1
            
        return max_window
