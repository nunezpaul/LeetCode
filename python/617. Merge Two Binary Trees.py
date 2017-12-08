'''
Given two binary trees and imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.

You need to merge them into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node. Otherwise, the NOT null node will be used as the node of new tree.

Example 1:
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree:
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
Note: The merging process must start from the root nodes of both trees.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        #initialize Binary Tree
        merged_tree = t1
        
        #if both t1_1 and t2_1 are real then the summation is the value of the t3_1
        if (t1 is not None) and (t2 is not None):
            merged_tree = TreeNode(t1.val+t2.val)
            
            #if either t1 or t2 has a left node then merge them, else do nothing
            if t1.left is not None or t2.left is not None:
                merged_tree.left = self.mergeTrees(t1.left, t2.left)
            
            #if either t1 or t2 has a right node then merge them, else do nothing
            if t1.right is not None or t2.right is not None:
                merged_tree.right = self.mergeTrees(t1.right, t2.right)
            
        elif (t1 is not None): #t2 is None therefore the value of t3_1 is t1_1
            merged_tree = TreeNode(t1.val)
            
            #if a left node exists then add that node and subsequent nodes
            if t1.left is not None: 
                merged_tree.left = t1.left
        
            #if a right node exists then add that node and subsequent nodes
            if t1.right is not None: 
                merged_tree.right = t1.right
                
        elif (t2 is not None): #t1 is None therefore the value of t3_1 is t2_1
            merged_tree = TreeNode(t2.val)
            
            #if a left node exists then add that node and subsequent nodes
            if t2.left is not None:
                merged_tree.left = t2.left
        
            #if a right node exists then add that node and subsequent nodes
            if t2.right is not None:
                merged_tree.right = t2.right
                
        else:
            pass
        
        return merged_tree
