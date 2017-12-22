/**

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

*/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
class Solution {
    public TreeNode invertTree(TreeNode root) {
        
        if (root != null) {
            
            if (root.left != null && root.right != null) {
                TreeNode hold = root.right;
                root.right = root.left;
                root.left = hold;
                root.right = invertTree(root.right);
                root.left = invertTree(root.left);
                
            } else if (root.left != null) {
                root.right = root.left;
                root.left = null;
                root.right = invertTree(root.right);
                
            } else if (root.right != null) {
                root.left = root.right;
                root.right = null;
                root.left = invertTree(root.left);
            }
        
          }
        return root;
        
        }
    }

/* runs faster than 15% of submissions
