# https://leetcode.com/problems/3sum/

class Solution:
    # Incorrerct 2-ptr implementation, doesn't consider terms 2 spaces away
    def threeSum(self, nums: List[int]) -> List[List[int]]:
	nums = sorted(nums)
        print(nums)
        size = len(nums)

        l = 0
        r = size-1
        result = []

        while l+1 < r:  # 'l-1' so there is always 3 vals present
            indices = [l, r]

            # Pull 3rd index
            if nums[l] + nums[r] < 0:   # Negative amount, needs pos
                indices.append(r-1)
            else:                       # Positive amount, needs neg
                indices.append(l+1)

            # Check
            vals = [nums[x] for x in indices]
            if sum(vals) == 0 and vals not in result:
                result.append(vals)

            # Update
            if sum(vals) < 0:   # Still negative, increment past most negative val
                l += 1
            else:               # Still positive, increment past most positive val
                r -= 1


        return result

   # Leetcode Solution, 2 ptrs
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i in range(len(nums)-2):               # Iterate through all values
            if i > 0 and nums[i] == nums[i-1]:          # Skip iteration if term is duplicate
                continue
            l, r = i+1, len(nums)-1                 # Get right & left ends beyond 'i'
            while l < r:                            # Iterate through all right & left nodes
                s = nums[i] + nums[l] + nums[r]
                if s < 0:                           # Increment/decrement ends until sum reached
                    l +=1 
                elif s > 0:
                    r -= 1
                else:                               # Add to res
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:   # Increment 'l' until no duplicate
                        l += 1
                    while l < r and nums[r] == nums[r-1]:   # dEcrement 'r' until no duplicate
                        r -= 1
                    l += 1; r -= 1                  # Final incre/decre to get past duplicate term
        return res

    # Leetcode solution, dividing into data structures based on +, -, and 0
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        res = set()

        #1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0: 
                n.append(num)
            else:
                z.append(num)

        #2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        #3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1*num in N:
                    res.add((-1*num, 0, num))

        #3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0,0,0))

        #4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))

        #5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        return res
