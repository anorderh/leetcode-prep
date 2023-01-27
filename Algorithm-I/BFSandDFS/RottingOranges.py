# https://leetcode.com/problems/rotting-oranges/description/?envType=study-plan&id=algorithm-i

class Solution:
    # Matrix with all rotten oranges cause rotting (sources) -> apply BFS
    def orangesRotting(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        mins = total = processed = 0 # Tracking total oranges vs. oranges processed
        queue = deque() 

        # Finding rotten indices & adding to queue
        for y in range(h):
            for x in range(w):
                if grid[y][x] != 0:  # Valid orange, increment tot.
                    total += 1 
                if grid[y][x] == 2:  # Rotten orange, increment processed & add to queue
                    queue.append((y,x))
                    processed += 1

        while queue:
            # Ensuring all oranges spread in same timeframe
            for _ in range(len(queue)): 
                dest = queue.popleft()

                for i, j in [(0,1),(0,-1),(1,0),(-1,0)]:    # Iterating thru adjacent coords
                    y, x = dest[0] + i, dest[1] + j

                    if y >= 0 and y < h and x >= 0 and x < w and grid[y][x] == 1: # Valid coords & fresh orange
                        grid[y][x] = 2

                        processed += 1
                        queue.append((y, x))

            mins += 1 if queue else 0 # Increment time after spreading
            
        
        return mins if processed == total else -1 # If processed != tot, fresh oranges remmain. Return -1, else return time
