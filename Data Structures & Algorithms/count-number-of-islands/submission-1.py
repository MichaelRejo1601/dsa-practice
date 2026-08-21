class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        y = len(grid)
        x = len(grid[0])
        count = 0 

        def _disqualifyConnectedLand_startingFrom(i,j):
            if i >= y or j >= x or i < 0 or j < 0:
                return 
            if grid[i][j] == '0':
                return 

            grid[i][j] = '0'
            _disqualifyConnectedLand_startingFrom(i+1,j)
            _disqualifyConnectedLand_startingFrom(i-1,j)
            _disqualifyConnectedLand_startingFrom(i,j+1)
            _disqualifyConnectedLand_startingFrom(i,j-1)
        
        for i in range(y):
            for j in range(x):
                if grid[i][j] == '1':
                    _disqualifyConnectedLand_startingFrom(i,j)
                    count += 1

        return count