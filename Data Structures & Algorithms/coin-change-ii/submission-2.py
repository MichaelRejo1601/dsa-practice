# You are given an integer array coins representing coins of different denominations (e.g. 1 dollar, 5 dollars, etc) and an integer amount representing a target amount of money.
# - coins[]
# - amount

# Return the number of distinct combinations that total up to amount. If it's impossible to make up the amount, return 0.
# - return num ways
# - if none, should return 0

# - coins are positive
# - len(coins) small 
# - amount medium 
# - coins[i] medium

# coins are positive 
# coins are unique 
# - taking a coin always decreases the amount left

# contraints:
# we need to figure out how many coins to use
# we don't need to use very coin
# order does not matter
# 122 vs 221 
# - have to avoid duplicates  
#    - kee track of counts?
#    - different orders 
#        - picking an order and sticking with it 
#        - allowed to sort


# You may assume that you have an unlimited number of each coin and that each value in coins is unique.
# - each coin is unique
# - unlimited number of coins 


# combinatorics?
# take or skip
# - reccurance 

# amount = 5 
# coins= [1,2,5]

# Decision
# find the number of ways to make amount using coins

# Starting with the ith coin what are my actions? 

# take the first coin
#  - amount = amount - coins[i] 
# skip the first coin
#  - have to move to the ith + 1 coin

# take i -> amount - coins[i]: take i, skip i
# skip i -> amount, take i +1, skip i+1


from functools import cache

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def numWays_toMake_startingWith(x: int, i:int)->int:
            if i == len(coins):
                return 1 if x == 0 else 0
            take = 0
            if x-coins[i] >= 0:
                take = numWays_toMake_startingWith(x-coins[i], i)
            skip = numWays_toMake_startingWith(x, i+1)
            return take + skip
        return numWays_toMake_startingWith(amount, 0)