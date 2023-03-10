class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        max_length = 0

        for n in nums:
            if n-1 not in unique: # no left neighbor, starting value found
                length = 1 

                while n+length in unique: # while val exists, increment
                    length += 1

                # compare w/ max
                max_length = max(max_length, length)

        return max_length
