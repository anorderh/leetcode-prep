# https://leetcode.com/problems/triangle/description/?envType=study-plan&id=algorithm-i

class Solution:
    # Dynamic programming deals with identifying recurrence relations
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Problem: Iterating from triangles top to bottom while accumulating the LEAST sum
        h = len(triangle)
        if h == 1:         
            return triangle[0][0]
        memory = [[-1 for y in range(1, x+1)] for x in range(1,h+1)]
        
        # Recurrence relation, focus on node ONE AT A TIME
        # Bc triangle constantly expanding, idx+1 is never invalid
        def branch(lvl, idx):
            if lvl >= h:    # If past triangle's floor, return 0
                return 0
            
            if memory[lvl][idx] != -1:  # If min path already found, return
                return memory[lvl][idx]
            
            res = min(      # Min of...
                triangle[lvl][idx] + branch(lvl+1, idx),    # (0,0) + min path at (lvl+1, idx)
                triangle[lvl][idx] + branch(lvl+1, idx+1))  # (0,0) + min path at (lvl+1, idx+1)
            # Because this is recursive, it will continue iterating for each node's minimum path

            memory[lvl][idx] = res      # Store min path
        
            return res
        
        # Origin -> (0,0)
        return branch(0, 0)
