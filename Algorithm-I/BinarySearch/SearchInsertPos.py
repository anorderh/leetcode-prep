# https://leetcode.com/problems/search-insert-position/?envType=study-plan&id=algorithm-i

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            cur = (low+high)//2

            if nums[cur] == target:
                return cur
            elif nums[cur] > target:
                high = cur-1
            else:
                low = cur+1

        return max(low,high)
