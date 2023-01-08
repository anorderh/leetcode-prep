class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        current = 0
        output = []
        for num in nums:
            current += num
            output.append(current)
        
        return output
