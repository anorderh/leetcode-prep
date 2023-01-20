# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan&id=algorithm-i

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # two pointers
        start = 0
        end = len(numbers) - 1

        while start < end:
            # total
            tot = numbers[start] + numbers[end]

            # numbers is sorted
            # -> increment 'start' raises 'tot'
            # -> decrement 'end' lowers 'tot
            if tot == target:
                return [start+1, end+1]
            elif tot > target:
                end -= 1
            else:
                start += 1
