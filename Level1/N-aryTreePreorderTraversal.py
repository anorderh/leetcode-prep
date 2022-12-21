# https://leetcode.com/problems/n-ary-tree-preorder-traversal/description/

# Unoptimized recursive solution, operating on each node's children if available and
appending value to list result

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if (root is None):
            return []
        
        traversal = [root.val]
        for child in root.children:
                traversal = traversal + self.preorder(child)
        return traversal

# Optimized iterative solution, iterating over children via a Stack for preorder traversal formatting

class Solution(object):
    def preorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if (root is None):
            return []

        stack = [root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.val)
            if (node.children != None):
                stack.extend(node.children[::-1])
        
        return result;
