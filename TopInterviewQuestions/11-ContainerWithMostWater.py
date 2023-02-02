# https://leetcode.com/problems/container-with-most-water/description/

class Solution:
    # Two Pointer approach, start with widest container
    def maxArea(self, height):
        i, j = 0, len(height) - 1 # start & ending indices
        water = 0
        while i < j:              
            # Water Amount = Water Level * Distance
            # -> Water Level is smallest height
            water = max(water, (j - i) * min(height[i], height[j]))

            # Now ptrs must be updated
            # -> Note that by iterating, we decrease the containers' width
            # -> Less wide containers require a higher water level
            # -> To ensure an increase, we remove from consideration the 
            # container's smallest height & its shackles on the Water Level

            # increment/decrement 'i' or 'j' based on which height smaller
            if height[i] < height[j]: 
                i += 1
            else:
                j -= 1
        return water
