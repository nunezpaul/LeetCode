'''

Invert a binary tree.
     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1
Trivia:
This problem was inspired by this original tweet by Max Howell:
Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so fuck off.

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
    
        if root is not None:
        
            if root.left is not None and root.right is not None:
                hold = root.left
                root.left = root.right
                root.right = hold
                root.left = self.invertTree(root.left)
                root.right = self.invertTree(root.right)
                    
            elif root.left is not None:
                root.right = root.left
                root.right = self.invertTree(root.right)
                root.left = None
                    
            elif root.right is not None:
                root.left = root.right
                root.left = self.invertTree(root.left)
                root.right = None
            
        return root

#runtime beats 94% of python submissions
