'''
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the number of edges between them.

Example 1:

Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:

2
Example 2:

Input:

              1
             / \
            4   5
           / \   \
          4   4   5
Output:

2
Note: The given binary tree has not more than 10000 nodes. The height of the tree is not more than 1000.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.longest = 0
        
    def checkLongestPath(self, value):
        if value > self.longest:
            self.longest = value
        
    def longestUnivaluePath(self, root, isHead = True):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        if root.left != None and root.right != None:
            left = self.longestUnivaluePath(root.left, isHead = False)
            right =self.longestUnivaluePath(root.right,isHead = False)
            
            
            
        elif root.right != None:
            right =self.longestUnivaluePath(root.right,isHead = False)
            left = 0
            
            
            
        elif root.left != None:
            right = 0
            left = self.longestUnivaluePath(root.left, isHead = False)
            
            
            
        else:
            right = 0
            left = 0

        if root.left != None and root.right != None and root.left.val == root.right.val and root.left.val == root.val:
            #add the two branches and return the largest between the two branches
            self.checkLongestPath(left+right+2)
            
            if isHead:
                return self.longest

            return max(left, right)+1
        
        elif root.left != None and root.left.val == root.val:
            self.checkLongestPath(left + 1)
            
            if isHead:
                return self.longest
            return left + 1
        
        elif root.right != None and root.right.val == root.val:
            self.checkLongestPath(right+1)
            
            if isHead:
                return self.longest

            return right+1
        
        else:
            
            if isHead:
                print('here', self.longest)
                return self.longest

            return 0
        
