import math

class Solution:
    def check_eatable(self, piles, k):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile/k)
        return hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      
        high = max(piles)
        low = 1
        res = high

        #check if min_k is valid, if not, check if min_k + min_k//2 is valid
        while low <= high:
            min_k = (low+high)//2
            
            if self.check_eatable(piles, min_k) <= h:
                res = min_k 
                high = min_k - 1 
            else: 
                low = min_k+1
        
        return res
            
            
