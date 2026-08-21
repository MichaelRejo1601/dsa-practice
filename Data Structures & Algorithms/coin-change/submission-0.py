# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.


# Return the fewest number of coins that you need to make up the exact target amount. If it is impossible to make up the amount, return -1.

# You may assume that you have an unlimited number of each coin.

# - positive integers
# - int array

# - return fewest num of coins to make amt
# if not return -1 

# ulimited coins

# coins len small
# coin amounts are huge
# amount is med

# left ->
# amount, i in the coin purse
# take the given coin amount=mount-coins[i]
# or skip it i+=1

# base case 
# i >= len(coins)

# return min()

from functools import cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @cache
        def fewestNumCoins_toMake_startingWith(amount, i) -> int:
            if i == len(coins):
                return 0 if amount == 0 else 100000

            take = 100000 
            if amount-coins[i] >= 0:
                take = 1+fewestNumCoins_toMake_startingWith(amount-coins[i], i)
            skip = fewestNumCoins_toMake_startingWith(amount, i+1)
            
            return min(take, skip)
        
        result = fewestNumCoins_toMake_startingWith(amount, 0)

        return result if result < 100000 else -1 