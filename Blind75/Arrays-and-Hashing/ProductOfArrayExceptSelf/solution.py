class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        ans = [1] * length

        # Tracking & storing num prefixes at every 'i' idx
        pre = 1
        for i in range(length):
            ans[i] = pre
            pre *= nums[i]
        
        # Tracking & applying num postfixes at every 'i' idx
        post = 1
        for i in range(length-1, -1, -1):
            ans[i] *= post
            post *= nums[i]
        
        return ans
