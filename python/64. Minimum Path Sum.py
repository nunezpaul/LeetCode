"""

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example 1:
[[1,3,1],
 [1,5,1],
 [4,2,1]]
Given the above grid map, return 7. Because the path 1→3→1→1→1 minimizes the sum.


O(mxn) solution

"""

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        #init by filling in for top row and left col:
        #only one path to enter them so we can fill that in at the beginning
        
        #grid[row][col] or grid[y][x]
        
        #fill in left col
        for i in range(1,len(grid)):
            grid[i][0] += grid[i-1][0]
                    
        #fill in top row
        for i in range(1, len(grid[0])):
            grid[0][i] += grid[0][i-1]
                        
                        
        #going through all the possibilities, we'll check if the number above or to the left is smaller
        #by selecting the number that's smallest then we'll have the shortest path
        for col in range(1, len(grid)):
            for row in range(1,len(grid[0])):
                grid[col][row] += min(grid[col-1][row], grid[col][row-1])
        
        return grid[-1][-1]
