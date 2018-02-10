'''
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
For example,

Consider the following matrix:

[
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
Given target = 3, return true.
'''

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        row = len(matrix)
        if row < 1:
            return False
        
        column = len(matrix[0])
        
        j = 0
        i = column-1
        
        #set up our boundary for our search matrix
        while i >= 0 and j <= row-1:

            if matrix[j][i] == target:
                return True
            
            elif matrix[j][i] > target:
                i-=1
                
            elif matrix[j][i] < target:
                j+=1
        
        #if we exceed any parameter then we hit the boundary and return False
        return False
            elif matrix[j][i] > target:
                i-=1
                
            elif matrix[j][i] < target:
                j+=1
        
        #if we exceed any parameter then we hit the boundary and return False
        return False
