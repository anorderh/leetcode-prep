class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() # Sort nums, groups dupes together

        # Iterate thru nums for 'base'
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i-1]: # If dupe found, skip iteration
                continue
            
            # Perform TwoSum using 2-ptr on remaining vals
            s, e = i+1, len(nums)-1
            while s < e: # Iterate until crossing
                new_sum = val + nums[s] + nums[e]

                if new_sum > 0: # Sum > 0, decre. 'e'
                    e -= 1
                elif new_sum < 0: # Sum < 0, incre. 's'
                    s += 1
                else: # Sum == 0, valid triplet
                    res.append([val, nums[s], nums[e]])
                    s += 1

                    # Dupe check -- Incre. 's' until non-dupe found
                    while nums[s] == nums[s-1] and s < e:
                        s += 1
        
        return res
