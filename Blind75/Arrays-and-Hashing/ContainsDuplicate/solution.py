class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mapping = set()

        for num in nums:
            if num in mapping: # Already present, dupe found
                return True
            else:
                mapping.add(num) # Add to mapping if not present

        return False
