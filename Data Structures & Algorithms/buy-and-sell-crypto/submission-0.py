class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_profit = 0 
        min_buy = prices[0]

        for sell in prices:
            best_profit = max(best_profit, sell-min_buy)
            min_buy = min(min_buy, sell)

        return best_profit