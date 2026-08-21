# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.

# Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.

# You may assume that you have an unlimited number of each coin and that each value in coins is unique.

# Using an array in ints, count combinations that sum up to an amount

# - len if coins is a small size
# - coins[i] and amount are meridum
# coins are unique
# coins are positive
# taking a coin always decreases the the amount
# return the number of combinations = counting problem
# - maybe combinatorics 
# 221 vs 112 (dedeplucate) if they have the same elements, but different orders
# - keep track of counts
# - pick and ordering and stick
# - allowed to sort



# - divisibility or GCD

# -reuse coins
# - when to stop? check before going negative

# Input: amount = 4, coins = [1,2,3]

# find the nuber of ways to make 4 using 1 2 and 3
# go left to right
# start with ith coin what are my actions

# take ith coin
#  take amount-coins[i] = amount
# skip ith coin
#  move to it+1 coin i + =1 

# amount = amount
# coins = coins


# make ammount using coins 


# starting with the ith coin


from functools import cache




class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        @cache
        def numWays_startingWith_toMake(amount, i) -> int:
            take = 0
            if i == len(coins):
                return 1 if amount == 0 else 0
            if amount - coins[i] >= 0:
                take = numWays_startingWith_toMake(amount-coins[i], i)
            skip = numWays_startingWith_toMake(amount, i+1)

            return take + skip

        return numWays_startingWith_toMake(amount, 0)