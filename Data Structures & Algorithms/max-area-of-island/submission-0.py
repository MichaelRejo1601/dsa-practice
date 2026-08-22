# You are given a matrix grid where grid[i] is either a 0 (representing water) or 1 (representing land).

# An island is defined as a group of 1's connected horizontally or vertically. You may assume all four edges of the grid are surrounded by water.

# The area of an island is defined as the number of cells within the island.

# Return the maximum area of an island in grid. If no island exists, return 0.

# water around


# 1 <= grid.length, grid[i].length <= 50

# return 0 if else

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        y = len(grid)
        x = len(grid[0])

        maxIsland = 0 

        def returnSize_ofIsland_andInvalidate(i,j):
            
            if i >= y or j >= x or i < 0 or j < 0:
                return 0
                
            if grid[i][j] == 0:
                return 0 
            
            grid[i][j] = 0 
            top = returnSize_ofIsland_andInvalidate(i-1,j)
            bottom = returnSize_ofIsland_andInvalidate(i+1,j)
            left = returnSize_ofIsland_andInvalidate(i,j-1)
            right = returnSize_ofIsland_andInvalidate(i,j+1)
            return 1 + top + bottom + left + right

        for i in range(y):
            for j in range(x):
                if grid[i][j] == 1:
                    maxIsland = max(returnSize_ofIsland_andInvalidate(i,j), maxIsland)
        
        return maxIsland

