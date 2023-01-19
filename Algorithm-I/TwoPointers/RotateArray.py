# https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        size = len(nums)
        k = k % size # {size} rotations is same as unaltered, so k = k%{size}
        if k < 0: # complement for negative rotations
            k += size 

        def reverse(start, end): # reverse sublist
            l = start
            r = end

            while l < r:
                temp = nums[l]
                nums[l] = nums[r]
                nums[r] = temp

                l += 1
                r -= 1

        reverse(0, size-k-1) # reverse sublist of ints not crossing
        reverse(size-k, size-1) # reverse sublist of ints crossing
        reverse(0, size-1) # reverse entire sublist
