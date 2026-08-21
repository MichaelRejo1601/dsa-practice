# There is an m x n grid
# - 2D Array

# You are allowed to move either down or to the right at any point in time. 
# - two options:
# move down 
# m + 1 
# move right
# n + 1


# Given the two integers m an n
# - give then bounds of the array 
# d = 0,m-1
# r = 0,n-1

# Return the number of possible unique paths that can be taken from the top-left corner of the grid to the bottom right
# - record: 
# numWays_fromPosition(x,y)
# take d or take r
# take d: d + 1, r remains same
# take r: d remains same, r + 1

# cache the solution to numWays_fromPosition(x,y)

# base case: 
# d=m-1
# r=n-1

# ret:
# take d + take r

# start at 0,0

# constraints:
# 1<m,n<100 
# small constraint

from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        def numWays_fromPosition(d,r):
            take_d = 0
            take_r = 0
            if d == m-1 and r == n-1:
                return 1
            if d != (m-1):
                take_d = numWays_fromPosition(d+1, r)
            if r != (n-1): 
                take_r = numWays_fromPosition(d, r+1)
            return take_d + take_r

        return numWays_fromPosition(0,0)