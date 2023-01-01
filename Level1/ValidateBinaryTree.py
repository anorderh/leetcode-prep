# https://leetcode.com/problems/validate-binary-search-tree/submissions/869196176/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def verify(node, low, high):
            if (node is None):
                return True
            elif (node.val >= high or node.val <= low):
                return False
            return verify(node.left, low, node.val) and verify(node.right, node.val, high)

        return verify(root, -inf, inf)
