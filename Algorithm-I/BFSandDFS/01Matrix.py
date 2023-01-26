# https://leetcode.com/problems/01-matrix/description/?envType=study-plan&id=algorithm-i

class Solution:
    # Breadth First Search to find each matrix's distance from a 0
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        h = len(mat)
        w = len(mat[0])

        # Helper method to find adjacent coordinates
        def neighbors(y, x):
            res = []
            res += [(y+i,x) for i in range(-1,2,2) if (y+i >= 0 and y+i < h)]
            res += [(y,x+i) for i in range(-1,2,2) if (x+i >= 0 and x+i < w)]

            return res

        queue = []

        # Adds all 0s to queue first
        # -> Iterate through non-zero nodes at SAME level
        # Use 'mat' to progressively count nodes' distances
        # Use '-1' to indicate "unprocessed" and assign to all non-zero values
        # -> When nodes distance is recorded, new value is used to indicate "processed"
        # -> Skips any 0s found when searching
        for y in range(h):
            for x in range(w):
                if (mat[y][x] == 0):
                    queue.append((y, x))
                else:
                    mat[y][x] = -1

        # DFS, iterating through search
        while queue:
            y, x = queue.pop(0)
            
            for new_y, new_x in neighbors(y, x):
                if mat[new_y][new_x] == -1:   # If '-1', process!
                    mat[new_y][new_x] = mat[y][x] + 1  # Increment new node by old node + 1
                    queue.append((new_y,new_x))
        
        return mat
