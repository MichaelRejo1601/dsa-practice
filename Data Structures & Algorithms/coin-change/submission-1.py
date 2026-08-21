# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

# Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

# You may assume that you have an unlimited number of each coin.

# integer array
# positive denominations

# fewest coins 

# make up target amount

# return -1 else

# unlimited of each coin (no order)


# 1 <= coins.length <= 10 small amount of coins
# 1 <= coins[i] <= 2^31 - 1 large coins
# 0 <= amount <= 10000 medium amount to make

# take = x - coins[i], i
# skip = x, i+1


# base case (amount is exceeded < 0) 
# base case amount is == 0 (return 1+)

from  functools import cache
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def fewestCoins_toMake_startingWith(x, i):
            
            if x == 0:
                return 0

            if i == len(coins) or x < 0:
                return float('inf')
            
            take = 1+fewestCoins_toMake_startingWith(x-coins[i], i)
            skip = fewestCoins_toMake_startingWith(x, i+1)
            return min(take, skip)

        res = fewestCoins_toMake_startingWith(amount, 0)

        return res if res != float('inf') else -1



