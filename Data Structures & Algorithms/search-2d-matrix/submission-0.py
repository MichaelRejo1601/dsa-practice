class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # first search
        l = 0
        r = len(matrix) - 1
        i = None #persist i
        while l <= r:
            i = (l+r)//2
            if matrix[i][0] > target:
                r = i - 1
            elif matrix[i][-1] < target:
                l = i + 1 
            else:
                break
        

        # second search
        l = 0
        r = len(matrix[0]) - 1
        j = None
        while l <= r:
            j = (l+r)//2
            if matrix[i][j] > target:
                r = j - 1
            elif matrix[i][j] < target:
                l = j + 1 
            else:
                return True

        return False