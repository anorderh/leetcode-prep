# https://leetcode.com/problems/move-zeroes/?envType=study-plan&id=algorithm-i

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        start = 0 # ptr for valid nums
        curr = 1 # ptr for 0's
        size = len(nums)

        while curr < size:
            if nums[start] != 0:
                start += 1
            elif nums[curr] != 0: # nums[start] is 0 and nums[curr] is valid num
                # swap curr and start
                nums[start], nums[curr] = nums[curr], nums[start]

                start += 1

            curr += 1

