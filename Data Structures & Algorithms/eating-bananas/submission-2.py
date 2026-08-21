import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def calculateHoursToEat(rate, piles):
            hours_per_pile = [math.ceil(pile/rate) for pile in piles]
            return sum(hours_per_pile)
        
        l = 1
        r = max(piles)
        result = None

        while l<=r:
            rate = (l+r)//2
            if calculateHoursToEat(rate, piles) > h:
                l = rate + 1
            elif calculateHoursToEat(rate, piles) <= h:
                result = rate
                r = rate - 1

        return result


