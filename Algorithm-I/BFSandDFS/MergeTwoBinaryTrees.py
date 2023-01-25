# https://leetcode.com/problems/merge-two-binary-trees/description/?envType=study-plan&id=algorithm-i

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if root1 is not None and root2 is not None: # Both roots exist, add to root1
            root1.val += root2.val
        else:            # Only 1 exists
            if root1 is None:
                return root2 
            else:
                return root1
        
        root1.right = self.mergeTrees(root1.right, root2.right)
        root1.left = self.mergeTrees(root1.left, root2.left)

        return root1

