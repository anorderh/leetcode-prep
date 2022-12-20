# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan&id=level-1

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        low = high = None
        difference = 0
        
        for price in prices:
            if (low is None or price < low):
                low = price
                high = None
            elif (high is None or price > high):
                high = price
                if (high - low) > difference:
                    difference = high - low
            
        return difference
