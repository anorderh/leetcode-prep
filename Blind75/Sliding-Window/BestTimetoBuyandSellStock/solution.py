class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy = None

        for i in range(len(prices)): # Process prices
            if buy is None or prices[i] < prices[buy]: # Set new buy-in if 1) None or 2) Costs less
                    buy = i
            else:   # Stock costs more, compare profit w/ cur max
                profit = max(profit, prices[i]-prices[buy])
        
        return profit
