# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        size = len(nums)
        result = [0] * size # to reverse iteration

        l = 0 # start ptr
        r = size - 1 # end ptr
        write = r # write ptr, starts from end to procure non-decreasing order

        while write >= 0:
            if abs(nums[l]) > abs(nums[r]): # add ^2 to result & increment l
                result[write] = nums[l]**2
                l += 1
            else:
                result[write] = nums[r]**2 # add ^2 to result & decrement r
                r -= 1
            # update loop condition
            write -= 1

        return result
