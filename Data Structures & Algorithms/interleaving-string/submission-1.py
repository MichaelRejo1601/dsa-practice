from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s3) != len(s1) + len(s2):
            return False
        
        @cache
        def returnTrue_ifInterleaveable(i, j, k):
            
            if k == len(s3) and i == len(s1) and j == len(s2):
                return True
            
            take_i = False 
            take_j = False

            if i < len(s1) and s1[i] == s3[k]:
                take_i = returnTrue_ifInterleaveable(i+1, j, k+1)
            if j < len(s2) and s2[j] == s3[k]:
                take_j = returnTrue_ifInterleaveable(i, j + 1, k+1)

            return take_i or take_j

        return returnTrue_ifInterleaveable(0,0,0)
        
























