
# Given a 2D grid grid where '1' represents land and '0' represents water, count and return the number of islands.

# An island is formed by connecting adjacent lands horizontally or vertically and is surrounded by water. You may assume water is surrounding the grid (i.e., all the edges are water).

# 1 <= grid.length, grid[i].length <= 100
# 100x100 grid maxs
# grid[i][j] is '0' or '1'.

# land or water
# return number ofislands
# what is an island?
# an island is horizontally or vertically connected AND surrounded by water.

# states: is island 1-n  (return true)
# not an island -1 (continue loop)
# continent (borders edge and not surrounded by water) 0 (must disqualify them) disqualify function (Return false)
# You may assume water is surrounding the grid nvm on the continents

#how will we traverse outwardsly when we find an items?
#recurrant function that identifies bounds with global variables
#graph? but that requires build it and theres no point
from functools import cache

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        x = len(grid[0])
        y = len(grid)
        hmap = {} #tracks islands (i,j) = islandno
        island_counter = 1

        @cache
        def _label_island_startingFrom(i,j):
            nonlocal x
            nonlocal y
            nonlocal island_counter

            if i >= y or j >= x or i < 0 or j < 0: 
                return

            if grid[i][j] == '1':
                hmap[(i,j)] = island_counter
                if hmap.get((i+1,j),0) == 0: 
                    _label_island_startingFrom(i+1,j)
                if hmap.get((i-1,j),0) == 0: 
                    _label_island_startingFrom(i-1,j)
                if hmap.get((i,j+1),0) == 0: 
                    _label_island_startingFrom(i,j+1)
                if hmap.get((i,j-1),0) == 0: 
                    _label_island_startingFrom(i,j-1)
            
            return #if water will return

        for i in range(y): #down
            for j in range(x): #right
                if grid[i][j] == '1' and hmap.get((i,j),0) == 0:
                    _label_island_startingFrom(i,j)
                    island_counter += 1
        
        return len(set(hmap.values()))
    
    


