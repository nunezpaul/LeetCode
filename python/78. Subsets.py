'''

Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

O(N*2**N)

'''

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        N = len(nums)
        answer = []
        
        for i in range(2**N): O(2**N)
            insertion = []
            create_guide = bin(i)[2:].zfill(N)
            
            for index, value in enumerate(create_guide): #O(N)
                if value == '1':
                    insertion.append(nums[index])
                    
            answer.append(insertion)
            
        return answer
