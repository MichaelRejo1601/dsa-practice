# You are given an integer array prices where prices[i] is the price of NeetCoin on the ith day.

# You may buy and sell one NeetCoin multiple times with the following restrictions:

# After you sell your NeetCoin, you cannot buy another one on the next day (i.e., there is a cooldown period of one day).
# - i = j+1, j = j+2
# You may only own at most one NeetCoin at a time.
# - must sell
# You may complete as many transactions as you like.
# - until i >= len(prices)

# Return the maximum profit you can achieve.
# - return sum of profits

#  Buy on day 0 (price = 1) and sell on day 1 (price = 3), profit = 3-1 = 2. 
#  Then buy on day 3 (price = 0) and sell on day 4 (price = 4), profit = 4-0 = 4. 
#  Total profit is 2 + 4 = 6.


# options: 
# take current sell (buy = sell + 2, sell = sell + 3) + profit
# increment sell 
# increment buy (if buy + 1 < sell)

from functools import cache

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        if len(prices) < 2:
            return 0
        @cache
        def maxProfit_buyingAt_sellingAt(i,j):
            
            if i >= len(prices) or j >= len(prices):
                return 0
            
            inc_buy = 0
            inc_sell = 0
            take = prices[j]-prices[i] + maxProfit_buyingAt_sellingAt(j+2, j+3)

            inc_sell = maxProfit_buyingAt_sellingAt(i, j+1)
            if i + 1 < j:
                inc_buy = maxProfit_buyingAt_sellingAt(i+1, j)
            
            return max(max(inc_buy,inc_sell), take)

        return maxProfit_buyingAt_sellingAt(0,1)
        