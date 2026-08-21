# You are given a 2-D grid of integers matrix, where each integer is greater than or equal to 0.

# Return the length of the longest strictly increasing path within matrix.
# #don't need to keep track of backtracking because strictly increasing will only ever move forward and never clash in on itself

# From each cell within the path, you can move either horizontally or vertically. You may not move diagonally.


# options

# take x+1, y
# take x-1, y
# take x, y+1 
# take x, y-1


from functools import cache

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        @cache        
        def maxLength_from(x,y):

            maxLength = 1

            for deltas in [(0,1),(0,-1),(1,0),(-1,0)]:
                new_x = x+deltas[0]
                new_y = y+deltas[1]
                if new_x < n and new_y < m and new_x >= 0 and new_y >= 0:
                    if matrix[x][y] < matrix[new_x][new_y]:
                        maxLength = max(maxLength, 1 + maxLength_from(new_x,new_y))

            return maxLength
        
        longest_path = 1

        for x in range(n):
            for y in range(m):
                longest_path = max(longest_path, maxLength_from(x,y))
        
        return longest_path