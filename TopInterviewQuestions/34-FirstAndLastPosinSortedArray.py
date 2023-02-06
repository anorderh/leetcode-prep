# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    # Given array of ints in increasing order, find starting & end position of given target value
    # EX:
    # Input: nums = [5,7,7,8,8,10], target = 8
    # Output: [3,4]
    # If not found, return [-1,-1]
    # Should work in O(log(n))
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(l, r, startingPos, goal):
            # action = "START" if startingPos else "END"
            # print(f"Starting BS on indices {l} and {r} for {action}")

            while l <= r:
                mid = (l+r)//2
                edge = mid-1 if startingPos else mid+1 # Finding left or right ends based on 'startingPos'
                # print(f"mid: {mid}, l: {l}, r: {r}")

                if nums[mid] == goal:   # Val found
                    if edge < 0 or edge >= size or nums[edge] != goal:  # Satisfy's edge check
                        return mid
                    elif startingPos:       # If looking for start, edge is on left
                        r = mid-1
                    else:                   # If looking for start, edge is on right
                        l = mid+1
                elif nums[mid] > goal:  # Check left side
                    r = mid-1
                else:                   # Check right side
                    l = mid+1
            return -1

        pos = [-1,-1]
        size = len(nums)
        if size == 1 and target == nums[0]:
            return [0,0]

        # Find start
        pos[0] = binarySearch(0, size-1, True, target)

        # Find end, skip if start is -1
        if pos[0] != -1:
            pos[1] = binarySearch(pos[0], size-1, False, target)
        
        return pos
        
