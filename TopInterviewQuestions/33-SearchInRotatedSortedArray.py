# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    # Binary Search, using most-left element to identify pivot location
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:     # target at mid
                return mid

            if nums[mid] >= nums[left]: # pivot rotated on left side
                if nums[left] <= target and target < nums[mid]: # Target is between 'left' and 'mid'?
                    # Focus on left
                    right = mid - 1  
                else:   
                    # Focus on right
                    left = mid + 1
            else:                       # pivot rotated on right side
                if nums[mid] < target and target <= nums[right]: # Target between 'mid' and 'right'?
                    # Focus on right
                    left = mid + 1
                else:
                    # Focus on left
                    right = mid - 1

        return -1
            
