# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/?envType=study-plan&id=algorithm-i

# DFS, 80% faster and 90% memory saved!

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        stack = []

        def iterate(node):
            if node is None: # If empty, return
                return

            if stack:                  # if queue not empty, pop element
                node.next = stack.pop()

            iterate(node.right) # iterating to most right element
            iterate(node.left) # checking left aftrewards
        
            stack.append(node)   # adding to queue
            
        iterate(root)
        return root
